from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  User, Student, Teacher, Guest, Coordinator
from .forms import  UsersForm, StudentsForm, TeachersForm, GuestsForm, CoordinatorsForm

# Create your views here.

@login_required
def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

@login_required
def teachers_new(request):
    if not request.user.is_staff:
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
    if not request.user.is_staff:
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
    if not request.user.is_staff:
        return render(request, 'statuses/401.html')

    teacher = get_object_or_404(Teacher, pk=id)

    if request.method == 'POST':
        teacher.user.delete()
        teacher.delete()
        return redirect('teachers_list')

    return render(request, 'teachers/teacher_delete_confirm.html', {'teacher': teacher})
