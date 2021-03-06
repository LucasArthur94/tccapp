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
from rooms import urls as rooms_urls
from events import urls as events_urls
from allocations import urls as allocations_urls
from evaluations import urls as evaluations_urls
from rules import urls as rules_urls
from scores import urls as scores_urls

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', include(home_urls)),
    path('users/', include(users_urls), name='users'),
    path('disciplines/', include(disciplines_urls), name='disciplines'),
    path('activities/<int:discipline_id>/', include(activities_urls), name='activities'),
    path('deliveries/<int:activity_id>/', include(deliveries_urls), name='deliveries'),
    path('workgroups/', include(workgroups_urls), name='workgroups'),
    path('rooms/', include(rooms_urls), name='rooms'),
    path('events/', include(events_urls), name='events'),
    path('allocations/<int:event_id>/', include(allocations_urls), name='allocations'),
    path('evaluations/<int:allocation_id>/', include(evaluations_urls), name='evaluations'),
    path('rules/', include(rules_urls), name='rules'),
    path('scores/<int:rule_id>/', include(scores_urls), name='scores'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('select2/', include(django_select2_urls)),
]
