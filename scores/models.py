from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rules.models import Rule
from workgroups.models import Workgroup

# Create your models here.

class Score(models.Model):
    REQUIRED_FIELDS = ('rule', 'workgroup', 'deliveries_average', 'theoretical_average', 'practical_average', 'final_score')

    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    workgroup = models.ForeignKey(Workgroup, on_delete=models.CASCADE)
    deliveries_average = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    theoretical_average = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    practical_average = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    final_score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
