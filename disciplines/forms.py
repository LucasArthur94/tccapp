from django.forms import ModelForm, DateInput
from users.models import User
from .models import  Discipline
from users.models import User
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget

class DisciplinesForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ['modality', 'users', 'start_date', 'end_date']
        labels = {
            'modality': _('Modalidade'),
            'users': _('Alunos'),
            'start_date': _('Data de Início'),
            'end_date': _('Data de Término'),
        }
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'users': ModelSelect2MultipleWidget(
                queryset=User.objects.filter(student__isnull=False),
                search_fields=['name__icontains', 'email__icontains']
            ),
        }
