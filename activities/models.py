from datetime import date
from django.db import models
from disciplines.models import Discipline

# Create your models here.

class Activity(models.Model):
    REQUIRED_FIELDS = ('name', 'weight', 'due_date', 'main_file_name', 'side_file_name', 'main_file_required', 'side_file_required', 'created_at', 'updated_at')

    name = models.CharField(
        max_length=100,
    )
    weight = models.IntegerField(
        default=1,
    )
    due_date = models.DateField()
    main_file_name = models.CharField(
        max_length=100,
        default='Documento Principal',
    )
    main_file_required = models.BooleanField(
        default=False
    )
    side_file_name = models.CharField(
        max_length=100,
        default='Documento Extra',
    )
    side_file_required = models.BooleanField(
        default=False
    )
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Activity methods
    def is_closed(self):
        return self.due_date < date.today()
