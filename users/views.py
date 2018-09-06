from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  User, Student, Teacher, Guest, Coordinator
from .forms import  TeachersForm, GuestsForm, CoordinatorsForm, StudentBulkRegisterForm
from .utils import xls_jupiter_parser

# Create your views here.

@login_required
def students_new_bulk(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    student_bulk_register_form = StudentBulkRegisterForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and student_bulk_register_form.is_valid():
        new_students_xls = request.FILES['students_xls']

        xls_jupiter_parser(new_students_xls)

        return redirect('disciplines_new')
    return render(request, 'students/new_bulk_form.html', {'student_bulk_register_form': student_bulk_register_form})


@login_required
def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

@login_required
def teachers_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    users_form = UsersForm(request.POST or None)
    teachers_form = TeachersForm(request.POST or None)

    if users_form.is_valid() and teachers_form.is_valid():
        new_user = users_form.save(commit=False)
        new_teacher = teachers_form.save(commit=False)

        new_user.is_staff = True
        new_user.username = new_user.email
        new_user.set_password(new_teacher.usp_number)
        new_user.save()

        new_teacher.user_id = new_user.pk
        new_teacher.save()

        return redirect('teachers_list')
    return render(request, 'teachers/teacher_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def teachers_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    teacher = get_object_or_404(Teacher, pk=id)
    teachers_form = TeachersForm(request.POST or None, request.FILES or None, instance=teacher)
    users_form = UsersForm(request.POST or None, request.FILES or None, instance=teacher.user)

    if users_form.is_valid() and teachers_form.is_valid():
        new_user = users_form.save(commit=False)
        new_user.username = new_user.email
        new_user.save()

        new_teacher = teachers_form.save()
        return redirect('teachers_list')

    return render(request, 'teachers/teacher_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def teachers_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    teacher = get_object_or_404(Teacher, pk=id)

    if request.method == 'POST':
        teacher.user.delete()
        teacher.delete()
        return redirect('teachers_list')

    return render(request, 'teachers/teacher_delete_confirm.html', {'teacher': teacher})
