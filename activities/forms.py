from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from datetime import date
from .models import  Activity
from django.utils.translation import gettext_lazy as _

class ActivitiesForm(ModelForm):
    def validate_retroative_date(value):
        if value < date.today():
            raise ValidationError(u'Insira uma data limite válida!')

    due_date = DateField(label='Data Limite de Entrega', validators=[validate_retroative_date])

    class Meta:
        model = Activity
        fields = ['name', 'weight', 'due_date', 'main_file_name', 'main_file_required', 'side_file_name', 'side_file_required']
        labels = {
            'name': _('Nome da Atividade'),
            'weight': _('Peso da Avaliação'),
            'main_file_name': _('Nome do Arquivo Principal'),
            'main_file_required': _('Arquivo Principal Necessário?'),
            'side_file_name': _('Nome do Arquivo Extra'),
            'side_file_required': _('Arquivo Extra Necessário?'),
        }
