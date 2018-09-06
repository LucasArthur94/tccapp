from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, FileField
from .models import  User, Student, Teacher, Guest, Coordinator
from django.utils.translation import gettext_lazy as _

class StudentBulkRegisterForm(Form):
    def validate_file_extension(value):
        if not value.name.endswith('.xls'):
            raise ValidationError(u'Insira um arquivo com extensão .xls')

    students_xls = FileField(validators=[validate_file_extension])

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
        fields = ['usp_number']
        labels = {
            'usp_number': _('Número USP'),
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
