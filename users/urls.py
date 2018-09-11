from django.urls import path
from .views import teachers_list, teachers_new, teachers_show, teachers_update, teachers_delete
from .views import students_new_bulk, students_list, students_new, students_show, students_update, students_delete
from .views import guests_list, guests_new, guests_show, guests_update, guests_delete

urlpatterns = [
    path('teachers/', teachers_list, name="teachers_list"),
    path('teachers/new/', teachers_new, name="teachers_new"),
    path('teachers/<int:id>', teachers_show, name="teachers_show"),
    path('teachers/update/<int:id>/', teachers_update, name="teachers_update"),
    path('teachers/delete/<int:id>/', teachers_delete, name="teachers_delete"),
    path('students/', students_list, name="students_list"),
    path('students/new/', students_new, name="students_new"),
    path('students/<int:id>', students_show, name="students_show"),
    path('students/update/<int:id>/', students_update, name="students_update"),
    path('students/delete/<int:id>/', students_delete, name="students_delete"),
    path('students/new/bulk/', students_new_bulk, name="students_new_bulk"),
    path('guests/', guests_list, name="guests_list"),
    path('guests/new/', guests_new, name="guests_new"),
    path('guests/<int:id>', guests_show, name="guests_show"),
    path('guests/update/<int:id>/', guests_update, name="guests_update"),
    path('guests/delete/<int:id>/', guests_delete, name="guests_delete"),
]
