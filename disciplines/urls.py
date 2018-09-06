from django.urls import path
from .views import disciplines_list, disciplines_new, disciplines_update, disciplines_delete

urlpatterns = [
    path('', disciplines_list, name="disciplines_list" ),
    path('new/', disciplines_new, name="disciplines_new" ),
    path('update/<int:id>/', disciplines_update, name="disciplines_update" ),
    path('delete/<int:id>/', disciplines_delete, name="disciplines_delete" ),
]
