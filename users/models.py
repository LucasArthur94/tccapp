from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'

    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        unique=True,
        db_index=True
    )

    objects = UserManager()

# User role models below

class Student(models.Model):
    """specific role model"""
    REQUIRED_FIELDS = ('user', 'usp_number', 'created_at', 'updated_at')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    usp_number = models.IntegerField(
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        data = {'name': self.user.name, 'appurl': 'https://tccapp-next-release.herokuapp.com'}
        html_email = render_to_string('users/emails/new_user.html', data)

        email = EmailMessage(
            subject='Bem-vindo a plataforma de TCC Poli USP',
            body=html_email,
            to=[self.user.email],
        )

        email.content_subtype = 'html'

        email.send()

class Teacher(models.Model):
    """specific role model"""
    REQUIRED_FIELDS = ('user', 'usp_number', 'created_at', 'updated_at')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    usp_number = models.IntegerField(
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)

        data = {'name': self.user.name, 'appurl': 'https://tccapp-next-release.herokuapp.com'}
        html_email = render_to_string('users/emails/new_user.html', data)

        email = EmailMessage(
            subject='Bem-vindo a plataforma de TCC Poli USP',
            body=html_email,
            to=[self.user.email],
        )

        email.content_subtype = 'html'

        email.send()


class Guest(models.Model):
    """specific role model"""
    REQUIRED_FIELDS = ('user', 'organization_name', 'created_at', 'updated_at')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    organization_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super(Guest, self).save(*args, **kwargs)

        data = {'name': self.user.name, 'appurl': 'https://tccapp-next-release.herokuapp.com'}
        html_email = render_to_string('users/emails/new_user.html', data)

        email = EmailMessage(
            subject='Bem-vindo a plataforma de TCC Poli USP',
            body=html_email,
            to=[self.user.email],
        )

        email.content_subtype = 'html'

        email.send()

class Coordinator(models.Model):
    """specific role model"""
    REQUIRED_FIELDS = ('user', 'usp_number', 'created_at', 'updated_at')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    usp_number = models.IntegerField(
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super(Coordinator, self).save(*args, **kwargs)

        data = {'name': self.user.name, 'appurl': 'https://tccapp-next-release.herokuapp.com'}
        html_email = render_to_string('users/emails/new_user.html', data)

        email = EmailMessage(
            subject='Bem-vindo a plataforma de TCC Poli USP',
            body=html_email,
            to=[self.user.email],
        )

        email.content_subtype = 'html'

        email.send()
