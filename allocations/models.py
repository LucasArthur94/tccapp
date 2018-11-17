from datetime import datetime
from django.db import models
from events.models import Event
from workgroups.models import Workgroup
from rooms.models import Room
from users.models import User

# Create your models here.

class Allocation(models.Model):
    REQUIRED_FIELDS = ('event', 'workgroup', 'selected_room', 'evaluators', 'start_time', 'end_time', 'created_at', 'updated_at')

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
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
