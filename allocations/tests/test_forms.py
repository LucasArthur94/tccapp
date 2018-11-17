from unittest import TestCase
from datetime import date, time, timedelta
from users.models import User, Student, Teacher, Guest
from events.models import Event
from disciplines.models import Discipline
from workgroups.models import Workgroup
from rooms.models import Room
from allocations.forms import AllocationsForm

class AllocationFormTestCase(TestCase):
    def test_valid_form(self):
        student_user = User.objects.create(username='alunogrupo@poli.usp.br', name="Aluno Teste", email='alunogrupo@poli.usp.br', password='7983131')
        student = Student.objects.create(usp_number='7983131', user=student_user)
        advisor_user = User.objects.create(username='professorgrupo@poli.usp.br', name="Professor Teste", email='professorgrupo@poli.usp.br', password='7918211')
        advisor = Teacher.objects.create(usp_number='7918211', user=advisor_user)
        guest_user = User.objects.create(username='convidadogrupo@poli.usp.br', name="Aluno Teste", email='convidadogrupo@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name='Empresa', user=guest_user)
        quarter_discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        quarter_discipline.users.add(student_user)
        semester_discipline = Discipline.objects.create(modality='SMS', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        semester_discipline.users.add(student_user)
        event = Event.objects.create(type='THR', quarter_discipline=quarter_discipline, semester_discipline=semester_discipline, selected_date=date.today() - timedelta(1), start_time=time(0, 0, 0), end_time=time(23, 59, 59))
        workgroup = Workgroup.objects.create(title='Grupo de Teste', advisor=advisor_user, guest=guest_user)
        workgroup.students.add(student_user)
        room = Room.objects.create(block='A', floor='T', identifier='ST')
        allocations_data = {'event': event, 'workgroup': workgroup, 'selected_room': room, 'evaluators': [advisor_user, guest_user], 'start_time': time(0, 0, 0), 'end_time': time(0, 20, 0)}
        allocation_form = AllocationsForm(data=allocations_data)
        self.assertTrue(allocation_form.is_valid())
