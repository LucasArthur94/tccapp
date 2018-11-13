from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from datetime import date
from .models import Event
from disciplines.models import Discipline
from rooms.models import Room
from django.utils import formats
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

class SemesterDisciplineWidget(ModelSelect2Widget):
    queryset = Discipline.objects.filter(modality__exact='SMS').order_by('-end_date')
    search_fields = ['end_date__icontains']

    def label_from_instance(self, obj):
        return "Início: " + str(formats.date_format(obj.start_date, "SHORT_DATE_FORMAT")) + " - Fim: " + str(formats.date_format(obj.end_date, "SHORT_DATE_FORMAT"))

class QuarterDisciplineWidget(ModelSelect2Widget):
    queryset = Discipline.objects.filter(modality__exact='QDR').order_by('-end_date')
    search_fields = ['end_date__icontains']

    def label_from_instance(self, obj):
        return "Início: " + str(formats.date_format(obj.start_date, "SHORT_DATE_FORMAT")) + " - Fim: " + str(formats.date_format(obj.end_date, "SHORT_DATE_FORMAT"))

class EventsForm(ModelForm):
    def validate_retroative_date(value):
        if value < date.today():
            raise ValidationError(u'Insira uma data válida!')

    selected_date = DateField(label='Data do Evento', validators=[validate_retroative_date])

    class Meta:
        model = Event
        fields = ['type', 'quarter_discipline', 'semester_discipline', 'weight', 'selected_date', 'start_time', 'end_time']
        labels = {
            'type': _('Tipo do Evento'),
            'quarter_discipline': _('Disciplina Quadrimestral Relacionada'),
            'semester_discipline': _('Disciplina Semestral Relacionada'),
            'weight': _('Peso da Nota do Evento'),
            'start_time': _('Hora de Início'),
            'end_time': _('Hora de Término'),
        }
        widgets = {
            'semester_discipline': SemesterDisciplineWidget,
            'quarter_discipline': QuarterDisciplineWidget
        }
