from django.urls import path
from .views import disciplines_list, disciplines_new

urlpatterns = [
    path('', disciplines_list, name="disciplines_list" ),
    path('new/', disciplines_new, name="disciplines_new" ),
]
