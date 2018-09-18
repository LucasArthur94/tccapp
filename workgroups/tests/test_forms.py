from unittest import TestCase
from users.models import User, Student, Teacher, Guest
from workgroups.forms import  WorkgroupsForm

class WorkgroupFormTestCase(TestCase):
    def test_valid_form(self):
        student_user = User.objects.create(username='alunogrupo@poli.usp.br', name="Aluno Teste", email='alunogrupo@poli.usp.br', password='7983131')
        student = Student.objects.create(usp_number='7983131', user=student_user)
        advisor_user = User.objects.create(username='professorgrupo@poli.usp.br', name="Professor Teste", email='professorgrupo@poli.usp.br', password='7918211')
        advisor = Teacher.objects.create(usp_number='7918211', user=advisor_user)
        guest_user = User.objects.create(username='convidadogrupo@poli.usp.br', name="Aluno Teste", email='convidadogrupo@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name='Empresa', user=guest_user)
        workgroups_data = {'title': 'Grupo de Teste', 'students': [student_user], 'advisor': advisor_user, 'guest': guest_user}
        workgroup_form = WorkgroupsForm(data=workgroups_data)
        self.assertTrue(workgroup_form.is_valid())
