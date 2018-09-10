from django.forms import ModelForm
from .models import Delivery
from django.utils.translation import gettext_lazy as _

class StudentsDeliveriesForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['main_file', 'side_file']
        labels = {
            'main_file': ('Arquivo Principal'),
            'side_file': ('Arquivo Extra'),
        }


class AdvisorsGuestsDeliveriesForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['public_comments', 'private_comments', 'score']
        labels = {
            'public_comments': ('Comentários Públicos'),
            'private_comments': ('Comentários Privados'),
            'score': ('Nota da Entrega'),
        }
