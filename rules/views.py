from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from decimal import Decimal
from .models import Rule
from .forms import RulesForm
from allocations.models import Allocation
from events.models import Event
from deliveries.models import Delivery
from evaluations.models import Evaluation
from scores.models import Score
from workgroups.models import Workgroup

# Create your views here.

@login_required
def rules_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rules = Rule.objects.all()
    return render(request, 'rules.html', {'rules': rules})

@login_required
def rules_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rules_form = RulesForm(request.POST or None)

    if rules_form.is_valid():
        rules_form.save()

        messages.success(request, 'Regra de cálculo de notas salva com sucesso!')
        return redirect('rules_list')
    return render(request, 'rule_form.html', {'rules_form': rules_form})

@login_required
def rules_show(request, id):
    rule = get_object_or_404(Rule, pk=id)

    return render(request, 'rule_show.html', {'rule': rule})

@login_required
def rules_run(request, id):
    rule = get_object_or_404(Rule, pk=id)

    workgroups = get_workgroups(rule)

    for workgroup in workgroups:
        deliveries_average = calculate_deliveries_average(workgroup)
        theoretical_average = calculate_theoretical_average(rule, workgroup)
        practical_average = calculate_practical_average(rule, workgroup)

        generate_score(deliveries_average, theoretical_average, practical_average, rule, workgroup)


    rule.last_runned_at = datetime.now()
    rule.save()

    rules = Rule.objects.all()

    messages.success(request, 'As notas para a regra desejada foram calculadas com sucesso!')
    return render(request, 'rules.html', {'rules': rules})

@login_required
def rules_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rule = get_object_or_404(Rule, pk=id)
    rules_form = RulesForm(request.POST or None, request.FILES or None, instance=rule)

    if rules_form.is_valid():
        rules_form.save()
        messages.success(request, 'Regra de cálculo de notas alterada com sucesso!')
        return redirect('rules_list')

    return render(request, 'rule_form.html', {'rules_form': rules_form})

@login_required
def rules_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rule = get_object_or_404(Rule, pk=id)

    if request.method == 'POST':
        rule.delete()
        messages.success(request, 'Regra de cálculo de notas excluída com sucesso!')
        return redirect('rules_list')

    return render(request, 'rule_delete_confirm.html', {'rule': rule})

# Private methods

def get_workgroups(rule):
    all_users = rule.quarter_discipline.users.all() | rule.semester_discipline.users.all()

    workgroups = []

    for user in all_users:
        related_workgroup = Workgroup.objects.filter(students__in=[user]).first()
        if related_workgroup:
            workgroups.append(related_workgroup)

    return workgroups

def calculate_deliveries_average(workgroup):
    deliveries = Delivery.objects.filter(Q(workgroup=workgroup), ~Q(status__exact = 'NAV')).order_by('-updated_at')

    total_score = Decimal(0.0)
    total_weight = 0
    readed_activities = []

    for delivery in deliveries:
        if delivery.activity not in readed_activities:
            total_score += delivery.score * delivery.activity.weight
            total_weight += delivery.activity.weight
            readed_activities.append(delivery.activity)

    return total_score / total_weight

def calculate_theoretical_average(rule, workgroup):
    allocation = Allocation.objects.filter(event=rule.theoretical_event, workgroup=workgroup).first()

    evaluations = Evaluation.objects.filter(allocation=allocation)

    total_score = Decimal(0.0)
    total_weight = 0

    for evaluation in evaluations:
        total_score += evaluation.sum()
        total_weight += 1

    return total_score / total_weight

def calculate_practical_average(rule, workgroup):
    allocation = Allocation.objects.filter(event=rule.practical_event, workgroup=workgroup).first()

    evaluations = Evaluation.objects.filter(allocation=allocation)

    total_score = Decimal(0.0)
    total_weight = 0

    for evaluation in evaluations:
        total_score += evaluation.sum()
        total_weight += 1

    return total_score / total_weight

def generate_score(deliveries_average, theoretical_average, practical_average, rule, workgroup):
    sum_score = deliveries_average + theoretical_average * rule.theoretical_event.weight + practical_average * rule.practical_event.weight
    sum_weight = (1 + rule.theoretical_event.weight + rule.practical_event.weight)

    final_score = sum_score / sum_weight

    score = Score.objects.filter(rule=rule, workgroup=workgroup).first()
    if score:
        score.deliveries_average = deliveries_average
        score.theoretical_average = theoretical_average
        score.practical_average = practical_average
        score.save()
    else:
        score = Score.objects.create(rule=rule, workgroup=workgroup, deliveries_average=deliveries_average, theoretical_average=theoretical_average, practical_average=practical_average, final_score=final_score)

        return score
