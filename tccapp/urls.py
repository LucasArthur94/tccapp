"""tccapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django_select2 import urls as django_select2_urls
from activities import urls as activities_urls
from deliveries import urls as deliveries_urls
from disciplines import urls as disciplines_urls
from home import urls as home_urls
from users import urls as users_urls
from workgroups import urls as workgroups_urls

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', include(home_urls)),
    path('users/', include(users_urls), name='users'),
    path('disciplines/', include(disciplines_urls), name='disciplines'),
    path('activities/<int:discipline_id>/', include(activities_urls), name='activities'),
    path('deliveries/<int:activity_id>/', include(deliveries_urls), name='deliveries'),
    path('workgroups/', include(workgroups_urls), name='workgroups'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('select2/', include(django_select2_urls)),
]
