from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from datetime import date
from django.utils import formats
from .models import  Rule
from users.models import User
from disciplines.models import Discipline
from events.models import Event
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget

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

class TheoreticalEventWidget(ModelSelect2Widget):
    queryset = Event.objects.filter(type__exact='THR').order_by('-selected_date')
    search_fields = ['selected_date__icontains']

    def label_from_instance(self, obj):
        return 'Banca Teórica - ' + str(formats.date_format(obj.selected_date, "SHORT_DATE_FORMAT"))

class PracticalEventWidget(ModelSelect2Widget):
    queryset = Event.objects.filter(type__exact='PRT').order_by('-selected_date')
    search_fields = ['selected_date__icontains']

    def label_from_instance(self, obj):
        return 'Feira Prática - ' + str(formats.date_format(obj.selected_date, "SHORT_DATE_FORMAT"))


class RulesForm(ModelForm):
    class Meta:
        model = Rule
        fields = ['quarter_discipline', 'semester_discipline', 'theoretical_event', 'practical_event']
        labels = {
            'quarter_discipline': _('Disciplina Quadrimestral Relacionada'),
            'semester_discipline': _('Disciplina Semestral Relacionada'),
            'theoretical_event': _('Banca Teórica'),
            'practical_event': _('Feira Prática'),
        }
        widgets = {
            'quarter_discipline': QuarterDisciplineWidget(),
            'semester_discipline': SemesterDisciplineWidget(),
            'theoretical_event': TheoreticalEventWidget(),
            'practical_event': PracticalEventWidget(),
        }
