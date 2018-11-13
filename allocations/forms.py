from django.db.models import Q
from django.forms import ModelForm
from datetime import datetime
from .models import Allocation
from users.models import User
from workgroups.models import Workgroup
from rooms.models import Room
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

class RoomWidget(ModelSelect2Widget):
    queryset = Room.objects.all()
    search_fields = ['block__icontains', 'floor__icontains', 'identifier__icontains']

    def label_from_instance(self, obj):
        return str(obj.block) + str(obj.floor) + " - " + str(obj.identifier)

class EvaluatorWidget(ModelSelect2MultipleWidget):
    queryset = User.objects.filter(Q(teacher__isnull=False) | Q(guest__isnull=False)).distinct()
    search_fields = ['name__icontains', 'email__icontains']

    def label_from_instance(self, obj):
        return str(obj.name)

class WorkgroupWidget(ModelSelect2Widget):
    queryset = Workgroup.objects.filter(created_at__year = datetime.now().year)
    search_fields = ['identifier__icontains', 'title__icontains']

    def label_from_instance(self, obj):
        if obj.modality == "SMS":
            modality = 'S'
        elif obj.modality == "QDR":
            modality = 'C'
        else:
            modality = 'M'

        return str(modality) + str(obj.identifier) + " - " + str(obj.title)

class AllocationsForm(ModelForm):
    class Meta:
        model = Allocation
        fields = ('workgroup', 'selected_room', 'evaluators', 'start_time', 'end_time')
        labels = {
            'workgroup': _('Grupo Alocado'),
            'selected_room': _('Sala Selecionada'),
            'evaluators': _('Avaliadores'),
            'start_time': _('Hora de Início'),
            'end_time': _('Hora de Término')
        }
        widgets = {
            'workgroup': WorkgroupWidget(),
            'selected_room': RoomWidget(),
            'evaluators': EvaluatorWidget()
        }
