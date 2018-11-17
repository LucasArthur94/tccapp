from unittest import TestCase
from events.models import Event
from disciplines.models import Discipline
from users.models import User, Student
from datetime import date, time, timedelta
from events.forms import EventsForm

# models test
class EventTestCase(TestCase):
    def test_valid_form(self):
        user = User.objects.create(username='aluno4@poli.usp.br', name="Aluno Teste", email='aluno4@poli.usp.br', password='9301293')
        student = Student.objects.create(usp_number='9301293', user=user)
        quarter_discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        quarter_discipline.users.add(user)
        semester_discipline = Discipline.objects.create(modality='SMS', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        semester_discipline.users.add(user)
        events_data = { 'type': 'THR', 'weight': 1, 'quarter_discipline': quarter_discipline, 'semester_discipline': semester_discipline, 'selected_date': date.today(), 'start_time': time(0, 0, 0), 'end_time': time(23, 59, 59) }
        event_form = EventsForm(data=events_data)
        self.assertTrue(event_form.is_valid())
