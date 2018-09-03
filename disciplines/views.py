import csv

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Discipline
from .forms import  DisciplinesForm, StudentBulkRegisterForm
from users.forms import UsersForm, StudentsForm

# Aux methods

def save_users_and_students(new_students_csv):
    file_data = new_students_csv.read().decode("utf-8")
    lines = file_data.split("\n")

    lines.pop(0)

    for line in lines:
        fields = line.split(",")
        user_dict = {}

        user_dict['name'] = fields[0]
        user_dict['email'] = fields[1]
        user_dict['username'] = fields[1]
        users_form = UsersForm(user_dict)

        if users_form.is_valid():
            recent_user = users_form.save(commit=False)
            recent_user.username = recent_user.email
            recent_user.save()

            student_dict = {}

            student_dict['usp_number'] = fields[2]
            student_dict['modality'] = fields[3]

            students_form = StudentsForm(student_dict)

            if students_form.is_valid():
                recent_student = students_form.save(commit=False)
                recent_student.user = recent_user
                recent_student.save()


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
    if not request.user.is_staff:
        return render(request, 'statuses/401.html')

    student_bulk_register_form = StudentBulkRegisterForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and student_bulk_register_form.is_valid():
        new_students_csv = request.FILES['students_csv']

        save_users_and_students(new_students_csv)

        disciplines_form = DisciplinesForm(request.POST or None)
        return render(request, 'discipline_form.html', {'disciplines_form': disciplines_form})

    return render(request, 'student_bulk_register_form.html', {'student_bulk_register_form': student_bulk_register_form})
