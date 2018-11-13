from unittest import TestCase
from datetime import date, timedelta
from users.models import User, Student
from disciplines.models import Discipline
from activities.forms import  ActivitiesForm

class ActivityFormTestCase(TestCase):
    def test_valid_form(self):
        user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='aluno@poli.usp.br', password='7654321')
        student = Student.objects.create(usp_number='7654321', user=user)
        discipline = Discipline.objects.create(modality="QDR", start_date=(date.today() - timedelta(8)), end_date=(date.today() - timedelta(1)))
        discipline.users.add(user)
        activities_data = {'name': 'Atividade de Teste', 'weight': 1, 'due_date': date.today(), 'main_file_name': 'Arquivo Principal', 'main_file_required': True, 'side_file_name': 'Arquivo Secundário','side_file_required': False, 'discipline': discipline}
        activity_form = ActivitiesForm(data=activities_data)
        self.assertTrue(activity_form.is_valid())
