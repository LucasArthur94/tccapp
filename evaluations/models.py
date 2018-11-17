from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from allocations.models import Allocation
from users.models import User

# Create your models here.

class Evaluation(models.Model):
    REQUIRED_FIELDS = ('allocation', 'owner', 'recommendation_for_best_project', 'presentation', 'arguing', 'implementation', 'documentation', 'private_comments', 'needs_fixes')

    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_for_best_project = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    presentation = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    arguing = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    implementation = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    documentation = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    private_comments = models.TextField(
        max_length=500,
        default='',
    )
    needs_fixes = models.BooleanField(
        default = False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Evaluation methods
    def is_closed(self):
        return self.end_time < datetime.now()

    def sum(self):
        return self.presentation + self.arguing + self.implementation + self.documentation
