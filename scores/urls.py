from django.urls import path
from .views import scores_list

urlpatterns = [
    path('', scores_list, name="scores_list" ),
]
