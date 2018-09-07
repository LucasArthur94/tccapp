from django.db import models
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from users.models import User

# Create your models here.

class Workgroup(models.Model):
    # Required fields
    REQUIRED_FIELDS = ('title', 'students', 'advisor', 'advisor_validated_participation')

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
