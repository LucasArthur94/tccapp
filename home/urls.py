from django.urls import path
from .views import home, logout_app, change_password

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_app, name="logout"),
    path('change-password/', change_password, name="change_password"),
]
