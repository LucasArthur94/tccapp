from django.urls import path
from .views import rules_list, rules_new, rules_show, rules_update, rules_run, rules_delete

urlpatterns = [
    path('', rules_list, name="rules_list" ),
    path('new/', rules_new, name="rules_new" ),
    path('<int:id>/', rules_show, name="rules_show" ),
    path('update/<int:id>/', rules_update, name="rules_update" ),
    path('run/<int:id>/', rules_run, name="rules_run" ),
    path('delete/<int:id>/', rules_delete, name="rules_delete" ),
]
