from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Room

class RoomsForm(ModelForm):
    class Meta:
        model = Room
        fields = ['block', 'floor', 'identifier']
        labels = {
            'block': _('Bloco'),
            'floor': _('Andar'),
            'identifier': _('Identificador da Sala'),
        }
