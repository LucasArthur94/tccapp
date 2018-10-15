from django.db import models
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from users.models import User

# Create your models here.

class Workgroup(models.Model):
    SEMESTER = 'SMS'
    QUARTELY = 'QDR'

    MODALITY_CHOICES = (
        (SEMESTER, 'Semestral'),
        (QUARTELY, 'Quadrimestral'),
    )

    # Required fields
    REQUIRED_FIELDS = ('modality', 'identifier', 'title', 'students', 'advisor', 'advisor_validated_participation')

    modality = models.CharField(
        max_length=3,
        choices=MODALITY_CHOICES,
        default=QUARTELY
    )
    identifier = models.IntegerField(
        default=1
    )
    title = models.CharField(
        max_length=100,
    )
    students = models.ManyToManyField(User, related_name='students')
    advisor = models.ForeignKey(User, related_name='workgroup_advisor',on_delete=models.CASCADE)
    advisor_validated_participation = models.BooleanField(
        default=False
    )
    guest = models.ForeignKey(User, related_name='workgroup_guest',on_delete=models.CASCADE, null=True, blank=True)
    guest_validated_participation = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # Workgroup methods
    def complete_identifier(self):
        if self.modality == 'SMS':
            return 'S' + str(self.identifier)
        elif self.modality == 'QDR':
            return 'C' + str(self.identifier)
        return None
