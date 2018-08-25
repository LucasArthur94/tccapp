from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  User, Student, Teacher, Guest, Coordinator
from .forms import  UsersForm, StudentsForm, TeachersForm, GuestsForm, CoordinatorsForm

# Create your views here.

@login_required
def users_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'users.html', {'teachers': teachers})

@login_required
def users_new(request):
    users_form = UsersForm(request.POST or None)
    teachers_form = TeachersForm(request.POST or None)

    if users_form.is_valid() and teachers_form.is_valid():
        new_user = users_form.save()
        new_teacher = teachers_form.save(commit=False)
        new_teacher.user_id = new_user.pk
        new_teacher.save()
        return redirect('users_list')
    return render(request, 'user_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def users_update(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    teachers_form = TeachersForm(request.POST or None, request.FILES or None, instance=teacher)
    users_form = UsersForm(request.POST or None, request.FILES or None, instance=teacher.user)

    if users_form.is_valid() and teachers_form.is_valid():
        new_user = users_form.save()
        new_teacher = teachers_form.save(commit=False)
        new_teacher.user_id = new_user.pk
        new_teacher.save()
        return redirect('users_list')
    print(users_form)
    return render(request, 'user_form.html', {'users_form': users_form, 'teachers_form': teachers_form})

@login_required
def users_delete(request, id):
    teacher = get_object_or_404(Teacher, pk=id)

    if request.method == 'POST':
        teacher.user.delete()
        teacher.delete()
        return redirect('users_list')

    return render(request, 'user_delete_confirm.html', {'teacher': teacher})
