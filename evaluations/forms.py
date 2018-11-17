from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.forms import ModelForm, ChoiceField
from django.forms.widgets import RadioSelect
from .models import Evaluation
from django.utils.translation import gettext_lazy as _

class TheoreticalEvaluationForm(ModelForm):
    CHOICES=[('0','0 (Não recomendo)'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5 (Recomendo muito)')]
    recommendation_for_best_project = ChoiceField(label = 'Recomenda para Melhor Projeto da Feira?', choices = CHOICES, widget = RadioSelect)


    class Meta:
        model = Evaluation
        fields = ['recommendation_for_best_project', 'presentation', 'arguing', 'implementation', 'documentation', 'needs_fixes', 'private_comments']
        labels = {
            'presentation': _('Nota da Apresentação (0,0 - 2,0)'),
            'arguing': _('Nota da Arguição (0,0 - 2,0)'),
            'implementation': _('Nota da Implementação (0,0 - 3,0)'),
            'documentation': _('Nota da Documentação (0,0 - 3,0)'),
            'needs_fixes': _('Necessita de Correções?'),
            'private_comments': _('Comentários e Correções'),
        }

    def clean_presentation(self):
        score = self.cleaned_data['presentation']
        if score < 0.0 or score > 2.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score

    def clean_arguing(self):
        score = self.cleaned_data['arguing']
        if score < 0.0 or score > 2.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score

    def clean_implementation(self):
        score = self.cleaned_data['implementation']
        if score < 0.0 or score > 3.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score

    def clean_documentation(self):
        score = self.cleaned_data['documentation']
        if score < 0.0 or score > 3.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score


class PracticalEvaluationForm(ModelForm):
    CHOICES=[('0','0 (Não recomendo)'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5 (Recomendo muito)')]
    recommendation_for_best_project = ChoiceField(label = 'Recomenda para Melhor Projeto da Feira?', choices = CHOICES, widget = RadioSelect)

    class Meta:
        model = Evaluation
        fields = ['recommendation_for_best_project', 'presentation', 'arguing', 'implementation', 'private_comments']
        labels = {
            'presentation': _('Nota da Apresentação (0,0 - 2,0)'),
            'arguing': _('Nota da Arguição (0,0 - 3,0)'),
            'implementation': _('Nota da Implementação (0,0 - 5,0)'),
            'private_comments': _('Correções Necessárias'),
        }

    def clean_presentation(self):
        score = self.cleaned_data['presentation']
        if score < 0.0 or score > 2.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score

    def clean_arguing(self):
        score = self.cleaned_data['arguing']
        if score < 0.0 or score > 3.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score

    def clean_implementation(self):
        score = self.cleaned_data['implementation']
        if score < 0.0 or score > 5.0:
            raise ValidationError(u'Preencha uma nota válida!')

        return score
