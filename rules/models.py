from datetime import date
from django.db import models
from disciplines.models import Discipline
from events.models import Event

# Create your models here.

class Rule(models.Model):
    REQUIRED_FIELDS = ('quarter_discipline', 'semester_discipline', 'theoretical_event', 'practical_event', 'last_runned_at')

    quarter_discipline = models.ForeignKey(Discipline, related_name='quarter_discipline', on_delete=models.CASCADE)
    semester_discipline = models.ForeignKey(Discipline, related_name='semester_discipline', on_delete=models.CASCADE)
    theoretical_event = models.ForeignKey(Event, related_name='theoretical_event', on_delete=models.CASCADE)
    practical_event = models.ForeignKey(Event, related_name='practical_event', on_delete=models.CASCADE)
    last_runned_at = models.DateTimeField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
