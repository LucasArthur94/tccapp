from django.urls import path
from .views import teachers_list, teachers_new, teachers_update, teachers_delete

urlpatterns = [
    path('teachers/', teachers_list, name="teachers_list"),
    path('teachers/new/', teachers_new, name="teachers_new"),
    path('teachers/update/<int:id>/', teachers_update, name="teachers_update"),
    path('teachers/delete/<int:id>/', teachers_delete, name="teachers_delete"),
]
