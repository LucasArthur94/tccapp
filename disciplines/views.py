from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Discipline
from .forms import  DisciplinesForm

# Create your views here.

@login_required
def disciplines_list(request):
    disciplines = Discipline.objects.all()
    return render(request, 'disciplines.html', {'disciplines': disciplines})

@login_required
def disciplines_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    disciplines_form = DisciplinesForm(request.POST or None)

    if disciplines_form.is_valid():
        disciplines_form.save()

        return redirect('disciplines_list')
    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_show(request, id):
    discipline = get_object_or_404(Discipline, pk=id)

    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')


    return render(request, 'discipline_show.html', {'discipline': discipline})

@login_required
def disciplines_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)
    disciplines_form = DisciplinesForm(request.POST or None, request.FILES or None, instance=discipline)

    if disciplines_form.is_valid():
        disciplines_form.save()
        return redirect('disciplines_list')

    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)

    if request.method == 'POST':
        discipline.delete()
        return redirect('disciplines_list')

    return render(request, 'discipline_delete_confirm.html', {'discipline': discipline})
