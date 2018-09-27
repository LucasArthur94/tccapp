from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_new_delivery_mail(new_delivery):
    data = {'appurl': settings.RUNNING_DOMAIN}
    html_email = render_to_string('emails/new_submission.html', data)

    destination_emails = [new_delivery.workgroup.advisor.email, new_delivery.workgroup.guest.email]

    email = EmailMessage(
        subject='Seu grupo de TCC enviou uma atividade!',
        body=html_email,
        to=destination_emails,
    )

    email.content_subtype = 'html'

    email.send()
