from datetime import datetime
from django.db import models
from events.models import Event
from workgroups.models import Workgroup
from rooms.models import Room
from users.models import User

# Create your models here.

class Evaluation(models.Model):
    THEORETICAL = 'THR'
    PRACTICAL = 'PRT'

    EVENT_TYPE_CHOICES = (
        (THEORETICAL, 'Banca Teórica'),
        (PRACTICAL, 'Banca Prática'),
    )

    REQUIRED_FIELDS = ('allocation', 'owner', 'type', 'nota1,2,3 e 4')

    type = models.ForeignKey(Event, on_delete=models.CASCADE)
    workgroup = models.ForeignKey(Workgroup, on_delete=models.CASCADE)
    selected_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    evaluators = models.ManyToManyField(User)
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Allocation methods
    def is_valid_time(self):
        return self.end_time > self.start_time

    def is_closed(self):
        return self.end_time < datetime.now()
