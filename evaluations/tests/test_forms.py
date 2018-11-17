from unittest import TestCase
from datetime import date, time, timedelta
from deliveries.models import Delivery
from activities.models import Activity
from allocations.models import Allocation
from disciplines.models import Discipline
from events.models import Event
from rooms.models import Room
from users.models import User, Student, Teacher, Guest
from workgroups.models import Workgroup
from evaluations.forms import  TheoreticalEvaluationForm, PracticalEvaluationForm

class TheoreticalEvaluationFormTestCase(TestCase):
    def test_valid_form(self):
        student_user = User.objects.create(username='alunogrupo21@poli.usp.br', name="Aluno Teste", email='alunogrupo21@poli.usp.br', password='7983333')
        student = Student.objects.create(usp_number='7983333', user=student_user)
        advisor_user = User.objects.create(username='professorgrupo32@poli.usp.br', name="Professor Teste", email='professorgrupo32@poli.usp.br', password='9818211')
        advisor = Teacher.objects.create(usp_number='9818211', user=advisor_user)
        guest_user = User.objects.create(username='convidadogrupo43@poli.usp.br', name="Aluno Teste", email='convidadogrupo43@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name='Empresa', user=guest_user)
        quarter_discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        quarter_discipline.users.add(student_user)
        semester_discipline = Discipline.objects.create(modality='SMS', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        semester_discipline.users.add(student_user)
        workgroup = Workgroup.objects.create(modality='QDR', identifier='1', title='Grupo de Teste', advisor=advisor_user)
        workgroup.students.add(student_user)
        event = Event.objects.create(type='THR', quarter_discipline=quarter_discipline, semester_discipline=semester_discipline, selected_date=date.today() + timedelta(1), start_time=time(0, 0, 0), end_time=time(23, 59, 59))
        room = Room.objects.create(block='A', floor='T', identifier='ST')
        allocation = Allocation.objects.create(event=event, workgroup=workgroup, selected_room=room, start_time=time(8, 20, 0), end_time=time(8, 50, 0))
        allocation.evaluators.add(advisor_user)
        allocation.evaluators.add(guest_user)
        theoretical_evaluation_data = {'recommendation_for_best_project': 1, 'arguing': 1.0, 'presentation': 1.0, 'implementation': 1.0, 'documentation': 1.0, 'private_comments': 'Gostei', 'needs_fixes': False}
        theoretical_evaluation_form = TheoreticalEvaluationForm(data=theoretical_evaluation_data)
        self.assertTrue(theoretical_evaluation_form.is_valid())

class PracticalEvaluationFormTestCase(TestCase):
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
        workgroup = Workgroup.objects.create(modality='QDR', identifier='1', title='Grupo de Teste', advisor=advisor_user)
        workgroup.students.add(student_user)
        event = Event.objects.create(type='THR', quarter_discipline=quarter_discipline, semester_discipline=semester_discipline, selected_date=date.today() + timedelta(1), start_time=time(0, 0, 0), end_time=time(23, 59, 59))
        room = Room.objects.create(block='A', floor='T', identifier='ST')
        allocation = Allocation.objects.create(event=event, workgroup=workgroup, selected_room=room, start_time=time(8, 20, 0), end_time=time(8, 50, 0))
        allocation.evaluators.add(advisor_user)
        allocation.evaluators.add(guest_user)
        practical_evaluation_data = {'recommendation_for_best_project': 1, 'arguing': 1.0, 'presentation': 1.0, 'implementation': 1.0, 'private_comments': 'Gostei'}
        practical_evaluation_form = PracticalEvaluationForm(data=practical_evaluation_data)
        self.assertTrue(practical_evaluation_form.is_valid())
