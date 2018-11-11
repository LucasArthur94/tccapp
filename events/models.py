from datetime import date
from django.db import models
from rooms.models import Room
from disciplines.models import Discipline

# Create your models here.
class Event(models.Model):
    THEORETICAL = 'THR'
    PRACTICAL = 'PRT'

    EVENT_TYPE_CHOICES = (
        (THEORETICAL, 'Banca Teórica'),
        (PRACTICAL, 'Banca Prática'),
    )

    # Required fields
    REQUIRED_FIELDS = ('type', 'disciplines', 'free_rooms', 'selected_date', 'start_time', 'end_time', 'created_at', 'updated_at')

    type = models.CharField(
        max_length=3,
        choices=EVENT_TYPE_CHOICES,
        default=THEORETICAL
    )
    disciplines = models.ManyToManyField(Discipline)
    free_rooms = models.ManyToManyField(Room)
    selected_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    weight = models.IntegerField(
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Event methods
    def is_valid_time(self):
        return self.end_time > self.start_time

    def is_retroative_time(self):
        return self.end_time < date.today()

    def event_type(self):
        if self.type == self.THEORETICAL:
            return 'Banca Teórica'
        elif self.type == self.PRACTICAL:
            return 'Feira Prática'
        else:
            return 'Evento Indefinido'
