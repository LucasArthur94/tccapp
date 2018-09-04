from django.forms import ModelForm, DateInput
from .models import  Activity
from django.utils.translation import gettext_lazy as _

class DateInput(DateInput):
    input_type = 'date'

class ActivitiesForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'weight', 'due_date', 'main_file_name', 'main_file_required', 'side_file_name', 'side_file_required']
        labels = {
            'name': ('Nome da Atividade'),
            'weight': ('Peso da Avaliação'),
            'due_date': ('Data Limite de Entrega'),
            'main_file_name': ('Nome do Arquivo Principal'),
            'main_file_required': ('Arquivo Principal Obrigatório?'),
            'side_file_name': ('Nome do Arquivo Extra'),
            'side_file_required': ('Arquivo Extra Obrigatório?'),
        }
        widgets = {
            'due_date': DateInput(),
        }
