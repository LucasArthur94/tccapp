from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from django.test.utils import override_settings
from django.urls import reverse_lazy
from datetime import date, timedelta
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from users.models import User, Coordinator, Teacher, Student, Guest
from disciplines.models import Discipline

@override_settings(DEBUG=True)
class NewActivityTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='1234567', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='alunogrupo2@poli.usp.br', password='7983121')
        student = Student.objects.create(usp_number='7983121', user=student_user)
        discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        discipline.users.add(user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('1234567')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_activity_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-disciplines').click()
        self.browser.find_element_by_id('manage-activities-1').click()
        self.browser.find_element_by_id('new-activity').click()

        self.browser.find_element_by_id('id_name').send_keys('Atividade de Teste')
        self.browser.find_element_by_id('id_weight').send_keys('2')
        self.browser.find_element_by_id('id_due_date').send_keys((date.today() - timedelta(2)).strftime('%d/%m/%Y'))

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("activities_list", kwargs={'discipline_id': 1}))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='card']/div[@class='card-header danger-color lighten-1 white-text'][contains(.,'Atividade de Teste - Fechada')]"))
