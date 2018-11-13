from django.db.models import Q
from django.forms import ModelForm, DateInput
from users.models import User
from .models import  Workgroup
from users.models import User
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

class StudentWidget(ModelSelect2MultipleWidget):
    queryset = User.objects.filter(student__isnull=False)
    search_fields = ['name__icontains', 'email__icontains']

    def label_from_instance(self, obj):
        return str(obj.name)

class TeacherWidget(ModelSelect2Widget):
    queryset = User.objects.filter(teacher__isnull=False)
    search_fields = ['name__icontains', 'email__icontains']

    def label_from_instance(self, obj):
        return str(obj.name)

class GuestWidget(ModelSelect2Widget):
    queryset = User.objects.filter(Q(teacher__isnull=False) | Q(guest__isnull=False)).distinct()
    search_fields = ['name__icontains', 'email__icontains']

    def label_from_instance(self, obj):
        return str(obj.name)

class WorkgroupsForm(ModelForm):
    class Meta:
        model = Workgroup
        fields = ['modality', 'identifier', 'title', 'students', 'advisor', 'guest']
        labels = {
            'modality': _('Modalidade'),
            'identifier': _('Número do Grupo'),
            'title': _('Título do Tema'),
            'students': _('Alunos'),
            'advisor': _('Orientador'),
            'guest': _('Co-orientador'),
        }
        widgets = {
            'students': StudentWidget(),
            'advisor': TeacherWidget(),
            'guest': GuestWidget(),
        }
