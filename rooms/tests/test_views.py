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

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='1234567', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='aluno@poli.usp.br', password='7654321')
        student = Student.objects.create(usp_number='7654321', user=student_user)

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('1234567')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_room_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-rooms').click()
        self.browser.find_element_by_id('new-room').click()

        modality_select = Select(self.browser.find_element_by_id("id_block"))
        modality_select.select_by_visible_text("Bloco A")

        modality_select = Select(self.browser.find_element_by_id("id_floor"))
        modality_select.select_by_visible_text("Térreo")

        self.browser.find_element_by_id('id_identifier').send_keys('ST')

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("rooms_list"))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='card']/div[@class='card-body elegant-color white-text rounded-bottom']/a[@class='white-text'][contains(.,'AT-ST')]"))
