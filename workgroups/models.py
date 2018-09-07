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

    def save(self, *args, **kwargs):
        super(Workgroup, self).save(*args, **kwargs)

        data = {'appurl': 'https://tccapp-next-release.herokuapp.com/workgroups'}
        html_email = render_to_string('emails/new_workgroup.html', data)

        destination_emails = [self.advisor.email]

        for student in self.students.all():
            destination_emails.append(student.email)

        if self.guest:
            destination_emails.append(self.guest.email)

        email = EmailMessage(
            subject='Você foi cadastrado em um grupo de projeto de formatura!',
            body=html_email,
            to=destination_emails,
        )

        email.content_subtype = 'html'

        email.send()
