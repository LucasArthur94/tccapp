from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.utils import override_settings
from django.urls import reverse_lazy
from selenium.webdriver import Chrome
from users.models import User, Coordinator, Teacher

@override_settings(DEBUG=True)
class SignUpTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='tccpoliusp', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('tccpoliusp')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_teacher_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-teachers').click()
        self.browser.find_element_by_id('new-teacher').click()
        self.browser.find_element_by_id('id_name').send_keys('Professor Teste')
        self.browser.find_element_by_id('id_email').send_keys('professor@poli.usp.br')
        self.browser.find_element_by_id('id_usp_number').send_keys('8765432')
        self.browser.find_element_by_id('submit').click()
        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("teachers_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[1][contains(.,'Professor Teste')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[2][contains(.,'professor@poli.usp.br')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[3][contains(.,'8765432')]"))

    def test_student_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-students').click()
        self.browser.find_element_by_id('new-student').click()
        self.browser.find_element_by_id('id_name').send_keys('Aluno Teste')
        self.browser.find_element_by_id('id_email').send_keys('aluno@poli.usp.br')
        self.browser.find_element_by_id('id_usp_number').send_keys('7654321')
        self.browser.find_element_by_id('submit').click()
        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("students_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[1][contains(.,'Aluno Teste')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[2][contains(.,'aluno@poli.usp.br')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[3][contains(.,'7654321')]"))

    def test_guest_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-guests').click()
        self.browser.find_element_by_id('new-guest').click()
        self.browser.find_element_by_id('id_name').send_keys('Convidado Teste')
        self.browser.find_element_by_id('id_email').send_keys('convidado@poli.usp.br')
        self.browser.find_element_by_id('id_organization_name').send_keys('Empresa Teste')
        self.browser.find_element_by_id('submit').click()
        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("guests_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[1][contains(.,'Convidado Teste')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[2][contains(.,'convidado@poli.usp.br')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[3][contains(.,'Empresa Teste')]"))
