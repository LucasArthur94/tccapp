from django.test import TestCase
from disciplines.models import Discipline
from users.models import User, Student
from datetime import date, timedelta

# models test
class DisciplineTestCase(TestCase):
    def test_is_closed(self):
        user = User.objects.create(username='aluno2@poli.usp.br', name="Aluno Teste", email='aluno2@poli.usp.br', password='7654321')
        student = Student.objects.create(usp_number='7654321', user=user)
        discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        discipline.users.add(user)
        self.assertTrue(isinstance(discipline, Discipline))
        self.assertTrue(discipline.is_closed())
