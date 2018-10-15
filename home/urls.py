from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import home, logout_app, change_password

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_app, name="logout"),
    path('change-password/', change_password, name="change_password"),
    path('password-reset/', PasswordResetView.as_view('html_email_template_name': 'registration/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
