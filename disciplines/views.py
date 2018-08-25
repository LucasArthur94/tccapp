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
    if not request.user.is_staff:
        return render(request, 'statuses/401.html')

    disciplines_form = DisciplinesForm(request.POST or None)

    if disciplines_form.is_valid():
        disciplines_form.save(commit=False)

        return redirect('disciplines_list')
    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})
