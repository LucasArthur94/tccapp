from django.urls import path
from .views import deliveries_list, deliveries_new

urlpatterns = [
    path('', deliveries_list, name="deliveries_list"),
    path('new/', deliveries_new, name="deliveries_new"),
]
