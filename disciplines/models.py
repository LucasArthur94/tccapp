from datetime import date
from django.db import models
from users.models import User

# Create your models here.

class Discipline(models.Model):
    SEMESTER = 'SMS'
    QUARTELY = 'QDR'

    MODALITY_CHOICES = (
        (SEMESTER, 'Semestral'),
        (QUARTELY, 'Quadrimestral'),
    )

    # Required fields
    REQUIRED_FIELDS = ('modality', 'users', 'start_date', 'end_date', 'created_at', 'updated_at')

    modality = models.CharField(
        max_length=3,
        choices=MODALITY_CHOICES,
        default=QUARTELY
    )
    users = models.ManyToManyField(User)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Discipline methods
    def is_valid_date(self):
        return self.end_date > self.start_date

    def is_closed(self):
        return self.end_date < date.today()
