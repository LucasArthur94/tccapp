from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Evaluation
from .forms import TheoreticalEvaluationForm, PracticalEvaluationForm
from workgroups.models import Workgroup
from allocations.models import Allocation

@login_required
def evaluations_list(request, allocation_id):
    if request.user.is_superuser:
        evaluations = Evaluation.objects.filter(allocation__id=allocation_id)
    else:
        evaluations = Evaluation.objects.filter(owner__id=request.user.pk, allocation__id=allocation_id)

    allocation = get_object_or_404(Allocation, pk=allocation_id)

    previous_evaluation = Evaluation.objects.filter(owner__id=request.user.pk, allocation__id=allocation_id).first()

    return render(request, 'evaluations.html', {'evaluations': evaluations, 'allocation': allocation, 'event_id': allocation.event.pk, 'previous_evaluation': previous_evaluation})

@login_required
def evaluations_show(request, allocation_id, id):
    allocation = get_object_or_404(Allocation, pk=allocation_id)

    evaluation = get_object_or_404(Evaluation, pk=id)

    if not allocation or not evaluation or request.user not in allocation.evaluators.all() or request.user != evaluation.owner:
        return render(request, 'statuses/401.html')

    return render(request, 'evaluation_show.html', {'evaluation': evaluation, 'allocation': allocation})

@login_required
def evaluations_new(request, allocation_id):
    previous_evaluation = Evaluation.objects.filter(owner__id=request.user.pk, allocation__id=allocation_id).first()

    allocation = get_object_or_404(Allocation, pk=allocation_id)

    if not allocation or request.user not in allocation.evaluators.all() or previous_evaluation or allocation.event.is_closed():
        return render(request, 'statuses/401.html')

    if allocation.event.is_theoretical():
        evaluations_form = TheoreticalEvaluationForm(request.POST or None, request.FILES or None)
    elif allocation.event.is_practical():
        evaluations_form = PracticalEvaluationForm(request.POST or None, request.FILES or None)
    else:
        return render(request, 'statuses/401.html')

    if evaluations_form.is_valid():
        new_evaluation = evaluations_form.save(commit=False)
        new_evaluation.owner_id = request.user.pk
        new_evaluation.allocation_id = allocation_id
        new_evaluation.save()

        return redirect('evaluations_list', allocation_id=allocation_id)
    return render(request, 'evaluation_form.html', {'evaluations_form': evaluations_form, 'allocation': allocation})

@login_required
def evaluations_update(request, allocation_id, id):
    evaluation = get_object_or_404(Evaluation, pk=id)

    allocation = get_object_or_404(Allocation, pk=allocation_id)

    if not allocation or request.user not in allocation.evaluators.all() or allocation.event.is_closed():
        return render(request, 'statuses/401.html')

    if allocation.event.is_theoretical:
        evaluations_form = TheoreticalEvaluationForm(request.POST or None, request.FILES or None, instance=evaluation)
    elif allocation.event.is_practical:
        evaluations_form = PracticalEvaluationForm(request.POST or None, request.FILES or None, instance=evaluation)
    else:
        return render(request, 'statuses/401.html')

    if evaluations_form.is_valid():
        new_evaluation = evaluations_form.save(commit=False)
        new_evaluation.owner_id = request.user.pk
        new_evaluation.allocation_id = allocation_id
        new_evaluation.save()

        return redirect('evaluations_list', allocation_id=allocation_id)
    return render(request, 'evaluation_form.html', {'evaluations_form': evaluations_form, 'allocation': allocation})

@login_required
def evaluations_delete(request, allocation_id, id):
    evaluation = get_object_or_404(Evaluation, pk=id)

    allocation = get_object_or_404(Allocation, pk=allocation_id)

    if not allocation or request.user not in allocation.evaluators.all() or allocation.event.is_closed():
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        evaluation.delete()
        return redirect('evaluations_list', allocation_id=allocation_id)

    return render(request, 'evaluation_delete_confirm.html', {'evaluation': evaluation, 'allocation': allocation})
