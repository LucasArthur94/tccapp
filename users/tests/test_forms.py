from unittest import TestCase

from users.models import User, Student, Teacher, Guest, Coordinator
from users.forms import  UsersForm, StudentsForm, TeachersForm, GuestsForm, CoordinatorsForm

class StudentFormTestCase(TestCase):
    def test_valid_form(self):
        user_data = {'username': 'aluno_novo@poli.usp.br', 'name': 'Aluno Teste', 'email': 'aluno_novo@poli.usp.br'}
        student_data = {'usp_number': '1111111'}
        user_form = UsersForm(data=user_data)
        student_form = StudentsForm(data=student_data)
        self.assertTrue(user_form.is_valid())
        self.assertTrue(student_form.is_valid())

    def test_invalid_form(self):
        user = User.objects.create(username='aluno2@poli.usp.br', name="Aluno Teste", email='aluno2@poli.usp.br', password='7654322')
        student = Student.objects.create(usp_number='7654322', user=user)
        user_data = {'username': user.username, 'name': user.name, 'email': user.email}
        student_data = {'usp_number': student.usp_number}
        user_form = UsersForm(data=user_data)
        student_form = StudentsForm(data=student_data)
        self.assertFalse(user_form.is_valid())
        self.assertFalse(student_form.is_valid())

class TeacherFormTestCase(TestCase):
    def test_valid_form(self):
        user_data = {'username': 'professor@poli.usp.br', 'name': 'Professor Teste', 'email': 'professor@poli.usp.br'}
        teacher_data = {'usp_number': '1234567'}
        user_form = UsersForm(data=user_data)
        teacher_form = TeachersForm(data=teacher_data)
        self.assertTrue(user_form.is_valid())
        self.assertTrue(teacher_form.is_valid())

    def test_invalid_form(self):
        user = User.objects.create(username='professor2@poli.usp.br', name="Professor Teste", email='professor2@poli.usp.br', password='7654321')
        teacher = Teacher.objects.create(usp_number='7654321', user=user)
        user_data = {'username': user.username, 'name': user.name, 'email': user.email}
        teacher_data = {'usp_number': teacher.usp_number}
        user_form = UsersForm(data=user_data)
        teacher_form = TeachersForm(data=teacher_data)
        self.assertFalse(user_form.is_valid())
        self.assertFalse(teacher_form.is_valid())

class GuestFormTestCase(TestCase):
    def test_valid_form(self):
        user_data = {'username': 'convidado@poli.usp.br', 'name': 'Convidado Teste', 'email': 'convidado@poli.usp.br'}
        guest_data = {'organization_name': 'Empresa Teste'}
        user_form = UsersForm(data=user_data)
        guest_form = GuestsForm(data=guest_data)
        self.assertTrue(user_form.is_valid())
        self.assertTrue(guest_form.is_valid())

    def test_invalid_form(self):
        user = User.objects.create(username='convidado2@poli.usp.br', name="Convidado Teste", email='convidado2@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name="Empresa Teste", user=user)
        user_data = {'username': user.username, 'name': user.name, 'email': user.email}
        guest_data = {'organization_name': 'Empresa Teste'}
        user_form = UsersForm(data=user_data)
        guest_form = GuestsForm(data=guest_data)
        self.assertFalse(user_form.is_valid())

class CoordinatorFormTestCase(TestCase):
    def test_valid_form(self):
        user_data = {'username': 'coordenador@poli.usp.br', 'name': 'Coordenador Teste', 'email': 'coordenador@poli.usp.br'}
        coordinator_data = {'usp_number': '1234567'}
        user_form = UsersForm(data=user_data)
        coordinator_form = CoordinatorsForm(data=coordinator_data)
        self.assertTrue(user_form.is_valid())
        self.assertTrue(coordinator_form.is_valid())

    def test_invalid_form(self):
        user = User.objects.create(username='coordenador2@poli.usp.br', name="Coordenador Teste", email='coordenador2@poli.usp.br', password='7654321')
        coordinator = Coordinator.objects.create(usp_number='7654321', user=user)
        user_data = {'username': user.username, 'name': user.name, 'email': user.email}
        coordinator_data = {'usp_number': coordinator.usp_number}
        user_form = UsersForm(data=user_data)
        coordinator_form = CoordinatorsForm(data=coordinator_data)
        self.assertFalse(user_form.is_valid())
        self.assertFalse(coordinator_form.is_valid())
