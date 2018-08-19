from django.shortcuts import render, redirect, get_object_or_404
from .models import  User, Student, Teacher, Guest, Coordinator
from .forms import  UsersForm, StudentsForm, TeachersForm, GuestsForm, CoordinatorsForm

# Create your views here.

def users_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def users_new(request):
    users_form = UsersForm(request.POST or None)
    teachers_form = TeachersForm(request.POST or None)

    if users_form.is_valid() and teachers_form.is_valid():
        new_user = users_form.save()
        new_teacher = teachers_form.save(commit=False)
        new_teacher.user_id = new_user.pk
        new_teacher.save()
        return redirect('users_list')
    return render(request, 'user_form.html', { 'users_form': users_form, 'teachers_form': teachers_form })
