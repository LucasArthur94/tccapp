from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from datetime import date
from .models import  Discipline
from users.models import User
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget

class DisciplinesForm(ModelForm):
    def validate_retroative_date(value):
        if value < date.today():
            raise ValidationError(u'Insira uma data de término válida!')

    start_date = DateField(label='Data de Início')
    end_date = DateField(label='Data de Término', validators=[validate_retroative_date])

    class Meta:
        model = Discipline
        fields = ['modality', 'users', 'start_date', 'end_date']
        labels = {
            'modality': _('Modalidade'),
            'users': _('Alunos'),
        }
        widgets = {
            'users': ModelSelect2MultipleWidget(
                queryset=User.objects.filter(student__isnull=False),
                search_fields=['name__icontains', 'email__icontains']
            ),
        }
