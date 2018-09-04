from django.urls import path
from .views import activities_list, activities_new, activities_update, activities_delete

urlpatterns = [
    path('', activities_list, name="activities_list" ),
    path('new/', activities_new, name="activities_new" ),
    path('update/<int:id>/', activities_update, name="activities_update" ),
    path('delete/<int:id>/', activities_delete, name="activities_delete" ),
]
