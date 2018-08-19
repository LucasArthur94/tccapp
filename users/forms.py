from django.forms import ModelForm
from .models import  User, Student, Teacher, Guest, Coordinator

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class StudentsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['usp_number', 'modality']

class TeachersForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['usp_number']

class GuestsForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['organization_name']

class CoordinatorsForm(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['usp_number']
