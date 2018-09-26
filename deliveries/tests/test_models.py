from django.test import TestCase
from deliveries.models import Delivery
from activities.models import Activity
from disciplines.models import Discipline
from workgroups.models import Workgroup
from users.models import User, Student, Teacher, Guest
from datetime import date, timedelta

# models test
class DeliveryTestCase(TestCase):
    def setUp(self):
        student_user = User.objects.create(username='alunogrupo@poli.usp.br', name="Aluno Teste", email='alunogrupo@poli.usp.br', password='7983131')
        student = Student.objects.create(usp_number='7983131', user=student_user)
        advisor_user = User.objects.create(username='professorgrupo@poli.usp.br', name="Professor Teste", email='professorgrupo@poli.usp.br', password='7918211')
        advisor = Teacher.objects.create(usp_number='7918211', user=advisor_user)
        guest_user = User.objects.create(username='convidadogrupo@poli.usp.br', name="Aluno Teste", email='convidadogrupo@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name='Empresa', user=guest_user)
        discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        discipline.users.add(student_user)
        activity = Activity.objects.create(name='Teste', due_date=date.today() - timedelta(1), main_file_name="Principal", side_file_name="Secundário", discipline=discipline)
        workgroup = Workgroup.objects.create(title='Grupo de Teste', advisor=advisor_user, guest=guest_user)
        workgroup.students.add(student_user)

    def test_is_avaliated_by_guest(self):
        student_user = User.objects.get(username='alunogrupo@poli.usp.br')
        workgroup = Workgroup.objects.get(title='Grupo de Teste')
        activity = Activity.objects.get(name='Teste')
        delivery = Delivery.objects.create(status="AGS", author=student_user, submission_date=date.today() - timedelta(1), workgroup=workgroup, activity=activity)
        self.assertTrue(isinstance(delivery, Delivery))
        self.assertTrue(delivery.is_avaliated_by_guest())

    def test_is_avaliated_by_advisor(self):
        student_user = User.objects.get(username='alunogrupo@poli.usp.br')
        workgroup = Workgroup.objects.get(title='Grupo de Teste')
        activity = Activity.objects.get(name='Teste')
        delivery = Delivery.objects.create(status="AAD", author=student_user, submission_date=date.today() - timedelta(1), workgroup=workgroup, activity=activity)
        self.assertTrue(isinstance(delivery, Delivery))
        self.assertTrue(delivery.is_avaliated_by_advisor())

    def test_is_avaliated(self):
        student_user = User.objects.get(username='alunogrupo@poli.usp.br')
        workgroup = Workgroup.objects.get(title='Grupo de Teste')
        activity = Activity.objects.get(name='Teste')
        delivery = Delivery.objects.create(status="AAD", author=student_user, submission_date=date.today() - timedelta(1), workgroup=workgroup, activity=activity)
        self.assertTrue(isinstance(delivery, Delivery))
        self.assertTrue(delivery.is_avaliated())
