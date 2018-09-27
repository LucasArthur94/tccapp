from django.db.models import Q
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from activities.models import Activity
from deliveries.models import Delivery
from disciplines.models import Discipline

# Create your views here.

def home(request):
    if hasattr(request.user, 'teacher') or hasattr(request.user, 'guest'):
        deliveries = Delivery.objects.filter(Q(workgroup__advisor=request.user) | Q(workgroup__guest=request.user)).order_by('-submission_date')

        return render(request, 'home.html', {'deliveries': deliveries})

    elif hasattr(request.user, 'student'):
        discipline = Discipline.objects.filter(users__in=[request.user]).order_by('-end_date').first()

        if discipline:
            activities = Activity.objects.filter(discipline__id=discipline.pk)
            return render(request, 'home.html', {'activities': activities, 'discipline_id': discipline.pk})

    return render(request, 'home.html')

def logout_app(request):
    logout(request)
    return redirect('home')
