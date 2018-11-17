from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
from django.test.utils import override_settings
from django.urls import reverse_lazy
from datetime import date, time, timedelta
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from users.models import User, Coordinator, Teacher, Student, Guest
from disciplines.models import Discipline

@override_settings(DEBUG=True)
class NewEventTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='1234567', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='alunogrupo2@poli.usp.br', password='7983121')
        student = Student.objects.create(usp_number='7983121', user=student_user)
        quarter_discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        quarter_discipline.users.add(user)
        semester_discipline = Discipline.objects.create(modality='SMS', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        semester_discipline.users.add(user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('1234567')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_activity_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-events').click()
        self.browser.find_element_by_id('new-event').click()

        modality_select = Select(self.browser.find_element_by_id("id_type"))
        modality_select.select_by_visible_text("Banca Teórica")

        self.browser.find_element_by_id("select2-id_quarter_discipline-container").send_keys('Início')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id("select2-id_semester_discipline-container").send_keys('Início')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id('id_selected_date').send_keys('01/01/2018')
        self.browser.find_element_by_id('id_start_time').send_keys(time(0, 0).strftime('%H:%M'))
        self.browser.find_element_by_id('id_end_time').send_keys(time(23, 59).strftime('%H:%M'))

        self.browser.find_element_by_id('id_weight').send_keys('2')

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("events_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='card']/div[@class='card-header danger-color lighten-1 white-text'][contains(.,'Evento Encerrado - 01/01/2018')]"))
