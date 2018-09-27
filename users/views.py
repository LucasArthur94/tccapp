from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  User, Student, Teacher, Guest, Coordinator
from .forms import  UsersForm, StudentsForm, TeachersForm, GuestsForm, CoordinatorsForm, StudentBulkRegisterForm
from .utils import xls_jupiter_parser, send_welcome_mail

# Teacher views

@login_required
def teachers_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

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

        send_welcome_mail(new_user)

        return redirect('teachers_list')
    return render(request, 'teachers/teacher_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def teachers_show(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    teacher = get_object_or_404(Teacher, pk=id)

    return render(request, 'teachers/teacher_show.html', {'teacher': teacher})

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

        teachers_form.save()
        return redirect('teachers_list')

    return render(request, 'teachers/teacher_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def teachers_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    teacher = get_object_or_404(Teacher, pk=id)

    if request.user.email == teacher.user.email:
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        teacher.user.delete()
        teacher.delete()
        return redirect('teachers_list')

    return render(request, 'teachers/teacher_delete_confirm.html', {'teacher': teacher})

# Student views

@login_required
def students_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})

@login_required
def students_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    users_form = UsersForm(request.POST or None)
    students_form = StudentsForm(request.POST or None)

    if users_form.is_valid() and students_form.is_valid():
        new_user = users_form.save(commit=False)
        new_student = students_form.save(commit=False)

        new_user.username = new_user.email
        new_user.set_password(new_student.usp_number)
        new_user.save()

        new_student.user_id = new_user.pk
        new_student.save()

        send_welcome_mail(new_user)

        return redirect('students_list')
    return render(request, 'students/student_form.html', {'users_form': users_form, 'students_form': students_form})

@login_required
def students_show(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    student = get_object_or_404(Student, pk=id)

    return render(request, 'students/student_show.html', {'student': student})

@login_required
def students_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    student = get_object_or_404(Student, pk=id)
    students_form = StudentsForm(request.POST or None, request.FILES or None, instance=student)
    users_form = UsersForm(request.POST or None, request.FILES or None, instance=student.user)

    if users_form.is_valid() and students_form.is_valid():
        new_user = users_form.save(commit=False)
        new_user.username = new_user.email
        new_user.save()

        students_form.save()
        return redirect('students_list')

    return render(request, 'students/student_form.html', {'users_form': users_form, 'students_form': students_form})

@login_required
def students_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    student = get_object_or_404(Student, pk=id)

    if request.user.email == student.user.email:
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        student.user.delete()
        student.delete()
        return redirect('students_list')

    return render(request, 'students/student_delete_confirm.html', {'student': student})

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

# Guest views

@login_required
def guests_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    guests = Guest.objects.all()
    return render(request, 'guests/guests.html', {'guests': guests})

@login_required
def guests_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    users_form = UsersForm(request.POST or None)
    guests_form = GuestsForm(request.POST or None)

    if users_form.is_valid() and guests_form.is_valid():
        new_user = users_form.save(commit=False)
        new_guest = guests_form.save(commit=False)

        new_user.username = new_user.email
        new_user.is_staff = True
        new_user.set_password('tccpoliusp')
        new_user.save()

        new_guest.user_id = new_user.pk
        new_guest.save()

        send_welcome_mail(new_user)

        return redirect('guests_list')
    return render(request, 'guests/guest_form.html', {'users_form': users_form, 'guests_form': guests_form})

@login_required
def guests_show(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    guest = get_object_or_404(Guest, pk=id)

    return render(request, 'guests/guest_show.html', {'guest': guest})

@login_required
def guests_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    guest = get_object_or_404(Guest, pk=id)
    guests_form = GuestsForm(request.POST or None, request.FILES or None, instance=guest)
    users_form = UsersForm(request.POST or None, request.FILES or None, instance=guest.user)

    if users_form.is_valid() and guests_form.is_valid():
        new_user = users_form.save(commit=False)
        new_user.username = new_user.email
        new_user.save()

        guests_form.save()
        return redirect('guests_list')

    return render(request, 'guests/guest_form.html', {'users_form': users_form, 'guests_form': guests_form})

@login_required
def guests_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    guest = get_object_or_404(Guest, pk=id)

    if request.user.email == guest.user.email:
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        guest.user.delete()
        guest.delete()
        return redirect('guests_list')

    return render(request, 'guests/guest_delete_confirm.html', {'guest': guest})
