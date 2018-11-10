from django.test import TestCase
from rooms.models import Room

# models test
class RoomTestCase(TestCase):
    def test_full_identifier(self):
        room = Room.objects.create(block='A', floor='T', identifier='ST')
        self.assertTrue(isinstance(room, Room))
        self.assertTrue(room.full_identifier() == 'AT-ST')
