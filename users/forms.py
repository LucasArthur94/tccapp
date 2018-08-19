from django.forms import ModelForm
from .models import  User, Student, Teacher, Guest, Coordinator
from django.utils.translation import gettext_lazy as _

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        labels = {
            'name': _('Nome'),
            'email': _('E-mail'),
        }

class StudentsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['usp_number', 'modality']
        labels = {
            'usp_number': _('Número USP'),
            'modality': _('Modalidade'),
        }

class TeachersForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['usp_number']
        labels = {
            'usp_number': _('Número USP'),
        }

class GuestsForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['organization_name']
        labels = {
            'organization_name': _('Nome da Empresa'),
        }

class CoordinatorsForm(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['usp_number']
        labels = {
            'usp_number': _('Número USP'),
        }
