from django.urls import path
from .views import deliveries_list, deliveries_list_by_workgroup, students_deliveries_new

urlpatterns = [
    path('', deliveries_list, name="deliveries_list"),
    path('workgroup/<int:workgroup_id>/', deliveries_list_by_workgroup, name="deliveries_list_by_workgroup"),
    path('workgroup/<int:workgroup_id>/new/', students_deliveries_new, name="students_deliveries_new"),
]
