from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField
from datetime import date
from .models import Event
from disciplines.models import Discipline
from rooms.models import Room
from django.utils import formats
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget

class RoomWidget(ModelSelect2MultipleWidget):
    queryset = Room.objects.all().order_by('-block')
    search_fields = ['block__icontains', 'floor__icontains', 'identifier__icontains']

    def label_from_instance(self, obj):
        return str(obj.block) + str(obj.floor) + "-" + str(obj.identifier)

class DisciplineWidget(ModelSelect2MultipleWidget):
    queryset = Discipline.objects.all().order_by('-end_date')
    search_fields = ['modality__icontains', 'end_date__icontains']

    def label_from_instance(self, obj):
        if obj.modality == "QDR":
            modality_text = 'Quadrimestral'
        elif obj.modality == "SMS":
            modality_text = 'Semestral'
        else:
            modality_text = 'Mágica'

        return "Início: " + str(formats.date_format(obj.start_date, "SHORT_DATE_FORMAT")) + " - " + modality_text

class EventsForm(ModelForm):
    def validate_retroative_date(value):
        if value > date.today():
            raise ValidationError(u'Insira uma data válida!')

    selected_date = DateField(label='Data do Evento', validators=[validate_retroative_date])

    class Meta:
        model = Event
        fields = ['type', 'disciplines', 'free_rooms', 'start_time', 'end_time']
        labels = {
            'type': _('Tipo do Evento'),
            'disciplines': _('Disciplinas Relacionadas'),
            'free_rooms': _('Salas Disponíveis'),
            'start_time': _('Hora de Início'),
            'end_time': _('Hora de Término'),
        }
        widgets = {
            'disciplines': DisciplineWidget,
            'free_rooms': RoomWidget
        }
