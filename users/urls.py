from django.urls import path
from .views import users_list, users_new, users_update, users_delete

urlpatterns = [
    path('list/', users_list, name="users_list"),
    path('new/', users_new, name="users_new"),
    path('update/<int:id>/', users_update, name="users_update"),
    path('delete/<int:id>/', users_delete, name="users_delete"),
]
