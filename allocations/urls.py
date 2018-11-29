from django.urls import path
from .views import allocations_list, allocations_new, allocations_show, allocations_update, allocations_delete, allocations_send_info_email

urlpatterns = [
    path('', allocations_list, name="allocations_list" ),
    path('new/', allocations_new, name="allocations_new" ),
    path('<int:id>/', allocations_show, name="allocations_show" ),
    path('update/<int:id>/', allocations_update, name="allocations_update" ),
    path('delete/<int:id>/', allocations_delete, name="allocations_delete" ),
    path('emails/', allocations_send_info_email, name="allocations_send_info_email" ),
]
