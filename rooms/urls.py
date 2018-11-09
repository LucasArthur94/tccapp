from django.urls import path
from .views import rooms_list, rooms_new, rooms_show, rooms_update, rooms_delete

urlpatterns = [
    path('', rooms_list, name="rooms_list"),
    path('new/', rooms_new, name="rooms_new"),
    path('<int:id>/', rooms_show, name="rooms_show"),
    path('update/<int:id>/', rooms_update, name="rooms_update"),
    path('delete/<int:id>/', rooms_delete, name="rooms_delete"),
]
