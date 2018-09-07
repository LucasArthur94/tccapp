from django.urls import path
from .views import workgroups_list, workgroups_new, workgroups_update, workgroups_delete, workgroups_confirm_participation

urlpatterns = [
    path('', workgroups_list, name="workgroups_list" ),
    path('new/', workgroups_new, name="workgroups_new" ),
    path('update/<int:id>/', workgroups_update, name="workgroups_update" ),
    path('delete/<int:id>/', workgroups_delete, name="workgroups_delete" ),
    path('confirm-participation/<int:id>/', workgroups_confirm_participation, name="workgroups_confirm_participation" ),
]
