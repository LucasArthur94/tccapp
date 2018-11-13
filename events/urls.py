from django.urls import path
from .views import events_list, events_new, events_show, events_update, events_delete

urlpatterns = [
    path('', events_list, name="events_list" ),
    path('new/', events_new, name="events_new" ),
    path('<int:id>/', events_show, name="events_show" ),
    path('update/<int:id>/', events_update, name="events_update" ),
    path('delete/<int:id>/', events_delete, name="events_delete" ),
]
