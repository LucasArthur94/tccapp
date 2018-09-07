import xlrd

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from users.forms import UsersForm, StudentsForm

def send_welcome_mail(user):
    data = {'name': user.name, 'appurl': 'https://tccapp-next-release.herokuapp.com'}
    html_email = render_to_string('users/emails/new_user.html', data)

    email = EmailMessage(
        subject='Bem-vindo a plataforma de TCC Poli USP',
        body=html_email,
        to=[user.email],
    )

    email.content_subtype = 'html'

    email.send()

def xls_jupiter_parser(new_students_xls):
    xls_path = default_storage.save('new_students.xls', ContentFile(new_students_xls.read()))
    spreadsheets = xlrd.open_workbook(xls_path)
    students_spreadsheet = spreadsheets.sheet_by_index(0)
    for row in range(6, students_spreadsheet.nrows):
        student_info = students_spreadsheet.row_slice(rowx=row, start_colx=0, end_colx=5)

        usp_number = student_info[0].value
        email = student_info[4].value

        if email and not '(P) ' in usp_number and not '(I) ' in usp_number:
            user_dict = {}

            user_dict['email'] = email
            user_dict['username'] = email
            user_dict['name'] = student_info[3].value
            users_form = UsersForm(user_dict)

            student_dict = {}
            student_dict['usp_number'] = usp_number
            students_form = StudentsForm(student_dict)

            if users_form.is_valid() and students_form.is_valid():
                recent_user = users_form.save(commit=False)
                recent_user.username = recent_user.email
                recent_user.set_password(usp_number)
                recent_user.save()

                recent_student = students_form.save(commit=False)
                recent_student.user = recent_user
                recent_student.save()

                send_welcome_mail(recent_user)

    default_storage.delete('new_students.xls')
