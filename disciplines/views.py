from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  Discipline
from .forms import  DisciplinesForm

# Create your views here.

@login_required
def disciplines_list(request):
    if request.user.is_superuser or request.user.is_staff:
        disciplines = Discipline.objects.all()
    else:
        disciplines = Discipline.objects.filter(users__in=[request.user]).distinct()
    return render(request, 'disciplines.html', {'disciplines': disciplines})

@login_required
def disciplines_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    disciplines_form = DisciplinesForm(request.POST or None)

    if disciplines_form.is_valid():
        disciplines_form.save()

        messages.success(request, 'Disciplina salva com sucesso!')
        return redirect('disciplines_list')
    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_show(request, id):
    discipline = get_object_or_404(Discipline, pk=id)

    return render(request, 'discipline_show.html', {'discipline': discipline})

@login_required
def disciplines_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)
    disciplines_form = DisciplinesForm(request.POST or None, request.FILES or None, instance=discipline)

    if disciplines_form.is_valid():
        disciplines_form.save()
        messages.success(request, 'Disciplina alterada com sucesso!')
        return redirect('disciplines_list')

    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)

    if request.method == 'POST':
        discipline.delete()
        messages.success(request, 'Disciplina excluída com sucesso!')
        return redirect('disciplines_list')

    return render(request, 'discipline_delete_confirm.html', {'discipline': discipline})
