from django.core.exceptions import ValidationError
from django.forms import Form, FileField, ModelForm, DateInput
from users.models import User
from .models import  Discipline
from users.models import User
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget

class DateInput(DateInput):
    input_type = 'date'

class DisciplinesForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ['modality', 'users', 'start_date', 'end_date']
        labels = {
            'modality': _('Modalidade'),
            'users': _('Usuários'),
            'start_date': _('Data de Início'),
            'end_date': _('Data de Término'),
        }
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'users': ModelSelect2MultipleWidget(
                model=User,
                search_fields=['name__icontains', 'email__icontains']
            ),
        }


class StudentBulkRegisterForm(Form):
    def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise ValidationError(u'Insira um arquivo com extensão .csv')

    students_csv = FileField(validators=[validate_file_extension])
