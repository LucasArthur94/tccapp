from django.urls import path
from .views import evaluations_list, evaluations_new, evaluations_show, evaluations_update, evaluations_delete

urlpatterns = [
    path('', evaluations_list, name="evaluations_list"),
    path('new/', evaluations_new, name="evaluations_new"),
    path('<int:id>/', evaluations_show, name="evaluations_show"),
    path('update/<int:id>/', evaluations_update, name="evaluations_update"),
    path('delete/<int:id>/', evaluations_delete, name="evaluations_delete"),
]
