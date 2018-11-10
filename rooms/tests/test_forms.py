from unittest import TestCase
from rooms.models import Room
from rooms.forms import  RoomsForm

class RoomFormTestCase(TestCase):
    def test_valid_form(self):
        room_data = {'block':'A', 'floor':'1', 'identifier':'01'}
        room_form = RoomsForm(data=room_data)
        self.assertTrue(room_form.is_valid())
