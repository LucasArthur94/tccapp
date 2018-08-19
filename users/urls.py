from django.urls import path
from .views import users_list, users_new

urlpatterns = [
    path('list/', users_list, name="users_list"),
    path('new/', users_new, name="users_new"),
]
