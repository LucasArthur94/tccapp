from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from disciplines.models import Discipline
from activities.models import Activity

# Create your views here.

def home(request):
    if request.user.student:
        discipline = Discipline.objects.filter(users__in=[request.user]).order_by('-end_date').first()
        activities = Activity.objects.filter(discipline__id=discipline.pk)

        return render(request, 'home.html', {'activities': activities, 'discipline_id': discipline.pk})

    return render(request, 'home.html')

def logout_app(request):
    logout(request)
    return redirect('home')
