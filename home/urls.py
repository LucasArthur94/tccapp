from django.urls import path
from .views import home, logout_app

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_app, name="logout"),
]
