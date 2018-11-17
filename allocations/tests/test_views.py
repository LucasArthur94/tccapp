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
from events.models import Event
from workgroups.models import Workgroup
from rooms.models import Room

@override_settings(DEBUG=True)
class NewAllocationTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(10)

        user = User.objects.create_user(username='admin@poli.usp.br', name="Administrador Teste", email='admin@poli.usp.br', password='1234567', is_staff=True, is_superuser=True)
        coordinator = Coordinator.objects.create(usp_number='1234567', user=user)
        teacher = Teacher.objects.create(usp_number='1234567', user=user)
        student_user = User.objects.create(username='aluno@poli.usp.br', name="Aluno Teste", email='alunogrupo2@poli.usp.br', password='7983121')
        student = Student.objects.create(usp_number='7983121', user=student_user)
        quarter_discipline = Discipline.objects.create(modality='QDR', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        quarter_discipline.users.add(student_user)
        semester_discipline = Discipline.objects.create(modality='SMS', start_date=date.today() - timedelta(8), end_date=date.today() - timedelta(1))
        semester_discipline.users.add(student_user)
        event = Event.objects.create(type='THR', quarter_discipline=quarter_discipline, semester_discipline=semester_discipline, selected_date=date.today() + timedelta(1), start_time=time(0, 0, 0), end_time=time(23, 59, 59))
        workgroup = Workgroup.objects.create(modality='QDR', identifier='1', title='Grupo de Teste', advisor=user)
        workgroup.students.add(student_user)
        room = Room.objects.create(block='A', floor='T', identifier='ST')

        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("login")))
        self.browser.find_element_by_id('id_username').send_keys('admin@poli.usp.br')
        self.browser.find_element_by_id('id_password').send_keys('1234567')
        self.browser.find_element_by_id('login').click()

    def tearDown(self):
        self.browser.quit()

    def test_allocation_sign_up_fire(self):
        self.browser.find_element_by_id('coordinator-events').click()
        self.browser.find_element_by_id('manage-allocations-1').click()
        self.browser.find_element_by_id('new-allocation').click()

        self.browser.find_element_by_id('id_start_time').send_keys(time(0, 0).strftime('%H:%M'))
        self.browser.find_element_by_id('id_end_time').send_keys(time(23, 59).strftime('%H:%M'))

        self.browser.find_element_by_class_name("select2-search__field").send_keys('administrador')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id("select2-id_workgroup-container").send_keys('C1')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.find_element_by_id("select2-id_selected_room-container").send_keys('A')
        self.browser.find_element_by_class_name("select2-results__option").click()

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.browser.find_element_by_id('submit').click()

        self.assertIn(('%s%s' % (self.live_server_url, reverse_lazy("allocations_list", kwargs={'event_id': 1}))), self.browser.current_url)
        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='card']/div[@class='card-header info-color lighten-1 white-text'][contains(.,'Grupo C1 - Sala AT-ST')]"))
