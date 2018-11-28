from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_new_allocation_mail(new_allocation):
    data = {'appurl': settings.RUNNING_DOMAIN, 'selectedDate': new_allocation.event.selected_date, 'startTime': new_allocation.start_time, 'endTime': new_allocation.end_time, 'room': new_allocation.selected_room.full_identifier()}
    html_email = render_to_string('emails/new_allocation.html', data)

    destination_emails = new_allocation.evaluators.values_list('email', flat=True)

    email = EmailMessage(
        subject='Você tem um evento marcado com os projetos de formatura do PCS!',
        body=html_email,
        to=destination_emails,
    )

    email.content_subtype = 'html'

    email.send()
