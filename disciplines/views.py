from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tablib import Dataset
from .models import  Discipline
from .forms import  DisciplinesForm, StudentBulkRegisterForm
from .resources import UserResource, StudentResource

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
        disciplines_form.save()

        return redirect('disciplines_list')
    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_update(request, id):
    if not request.user.is_staff:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)
    disciplines_form = DisciplinesForm(request.POST or None, request.FILES or None, instance=discipline)

    if disciplines_form.is_valid():
        disciplines_form.save()
        return redirect('disciplines_list')

    return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

@login_required
def disciplines_delete(request, id):
    if not request.user.is_staff:
        return render(request, 'statuses/401.html')

    discipline = get_object_or_404(Discipline, pk=id)

    if request.method == 'POST':
        discipline.delete()
        return redirect('disciplines_list')

    return render(request, 'discipline_delete_confirm.html', {'discipline': discipline})

@login_required
def student_bulk_register(request):
    if request.method == 'POST':
        student_bulk_register_form = StudentBulkRegisterForm(request.POST or None, request.FILES or None)

        if student_bulk_register_form.is_valid():
            user_resource = UserResource()
            student_resource = StudentResource()
            dataset = Dataset()
            new_students = request.FILES['students_csv']

            print(new_students)

            imported_data = dataset.load(new_students.read())

            users_result = user_resource.import_data(dataset, dry_run=True)
            students_result = student_resource.import_data(dataset, dry_run=True)

            if not users_result.has_errors() and not students_result.has_errors():
                user_resource.import_data(dataset, dry_run=False)
                student_resource.import_data(dataset, dry_run=False)

            disciplines_form = DisciplinesForm(request.POST or None)
            return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

    return render(request, 'student_bulk_register_form.html', {'student_bulk_register_form': student_bulk_register_form})
