import xlrd

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_new_workgroup_mail(workgroup):
    data = {'appurl': 'https://tccapp-next-release.herokuapp.com/workgroups'}
    html_email = render_to_string('emails/new_workgroup.html', data)

    destination_emails = [workgroup.advisor.email]

    for student in workgroup.students.all():
        destination_emails.append(student.email)

    if workgroup.guest:
        destination_emails.append(workgroup.guest.email)

    email = EmailMessage(
        subject='Você foi cadastrado em um grupo de projeto de formatura!',
        body=html_email,
        to=destination_emails,
    )

    email.content_subtype = 'html'

    email.send()
