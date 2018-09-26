from django.test import TestCase
from activities.models import Activity
from disciplines.models import Discipline
from users.models import User, Student
from datetime import date, timedelta

# models test
class ActivityTestCase(TestCase):
    def test_is_closed(self):
        user = User.objects.create(username='aluno4@poli.usp.br', name="Aluno Teste", email='aluno4@poli.usp.br', password='9301293')
        student = Student.objects.create(usp_number='9301293', user=user)
        discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        discipline.users.add(user)
        activity = Activity.objects.create(name='Teste', due_date=date.today() - timedelta(1), main_file_name="Principal", side_file_name="Secundário", discipline=discipline)
        self.assertTrue(isinstance(activity, Activity))
        self.assertTrue(activity.is_closed())
