from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from django.test.utils import override_settings
from django.urls import reverse_lazy
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from users.models import User, Coordinator, Teacher, Student

@override_settings(DEBUG=True)
class NewDisciplineTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='tccpoliusp', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='aluno@poli.usp.br', password='7654321')
        student = Student.objects.create(usp_number='7654321', user=student_user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('tccpoliusp')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    @skip("Quantic test to fix it")
    def test_teacher_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-disciplines').click()
        self.browser.find_element_by_id('new-discipline').click()

        modality_select = Select(self.browser.find_element_by_id("id_modality"))
        modality_select.select_by_visible_text("Semestral")

        self.browser.find_element_by_class_name("select2-search__field").send_keys('aluno')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id('id_start_date').send_keys('01012018')
        self.browser.find_element_by_id('id_end_date').send_keys('30042018')

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("disciplines_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[1][contains(.,'Semestral')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[2][contains(.,'0')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[3][contains(.,'1 de Janeiro de 2018')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//table[@class='table']/tbody/tr/th[4][contains(.,'30 de Abril de 2018')]"))
