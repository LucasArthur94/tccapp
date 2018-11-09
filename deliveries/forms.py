from django.forms import ModelForm, widgets
from django.forms.widgets import HiddenInput
from .models import Delivery
from django.utils.translation import gettext_lazy as _

class StudentsDeliveriesForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['main_file', 'side_file']
        labels = {
            'main_file': _('Arquivo Principal'),
            'side_file': _('Arquivo Extra'),
            'submission_comments': _('Comentários da Entrega')
        }

    def __init__(self, activity=None, *args, **kwargs):
        super(StudentsDeliveriesForm, self).__init__(*args, **kwargs)
        if activity:
            self.fields['main_file'].label = activity.main_file_name
            self.fields['main_file'].required = activity.main_file_required
            if not activity.main_file_required:
                self.fields['main_file'].widget = HiddenInput()

            self.fields['side_file'].label = activity.side_file_name
            self.fields['side_file'].required = activity.side_file_required
            if not activity.side_file_required:
                self.fields['side_file'].widget = HiddenInput()



class AdvisorsGuestsDeliveriesForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['score', 'public_comments', 'private_comments']
        labels = {
            'public_comments': ('Comentários Públicos'),
            'private_comments': ('Comentários Privados'),
            'score': ('Nota da Entrega'),
        }
