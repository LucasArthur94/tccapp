from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from django.test.utils import override_settings
from django.urls import reverse_lazy
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from users.models import User, Coordinator, Teacher, Student, Guest

@override_settings(DEBUG=True)
class NewWorkgroupTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='tccpoliusp', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='alunogrupo2@poli.usp.br', name="Aluno Teste", email='alunogrupo2@poli.usp.br', password='7983121')
        student = Student.objects.create(usp_number='7983121', user=student_user)
        guest_user = User.objects.create(username='convidadogrupo2@poli.usp.br', name="Convidado Teste", email='convidadogrupo2@poli.usp.br', password='7654321')
        guest = Guest.objects.create(organization_name='Empresa', user=guest_user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('tccpoliusp')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_teacher_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-workgroups').click()
        self.browser.find_element_by_id('new-workgroup').click()

        self.browser.find_element_by_id('id_title').send_keys('Projeto de Teste')

        self.browser.find_element_by_class_name("select2-search__field").send_keys('alunogrupo')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_class_name("select2-search__field").send_keys('admin')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_class_name("select2-search__field").send_keys('convidadogrupo')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("disciplines_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[1][contains(.,'Projeto de Teste')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[2][contains(.,'1')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[3][contains(.,'Administrador Teste')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[4][contains(.,'Convidado Teste')]"))
