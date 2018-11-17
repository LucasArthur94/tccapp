from unittest import TestCase
from datetime import date, timedelta
from users.models import User, Student, Teacher, Guest, Coordinator
from disciplines.forms import  DisciplinesForm

class DisciplineFormTestCase(TestCase):
    def test_valid_form(self):
        user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='aluno@poli.usp.br', password='7654321')
        student = Student.objects.create(usp_number='7654321', user=user)
        discipline_data = {'modality': 'QDR', 'start_date': date.today() - timedelta(8), 'end_date': date.today() - timedelta(1), 'users': [user]}
        discipline_form = DisciplinesForm(data=discipline_data)
        self.assertTrue(discipline_form.is_valid())
