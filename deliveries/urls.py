from django.urls import path
from .views import deliveries_list, deliveries_new, deliveries_show, deliveries_update, deliveries_review, deliveries_delete

urlpatterns = [
    path('', deliveries_list, name="deliveries_list"),
    path('new/', deliveries_new, name="deliveries_new"),
    path('<int:id>/', deliveries_show, name="deliveries_show"),
    path('update/<int:id>/', deliveries_update, name="deliveries_update"),
    path('review/<int:id>/', deliveries_review, name="deliveries_review"),
    path('delete/<int:id>/', deliveries_delete, name="deliveries_delete"),
]
