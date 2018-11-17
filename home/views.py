from django.db.models import Q
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from activities.models import Activity
from allocations.models import Allocation
from deliveries.models import Delivery
from disciplines.models import Discipline

# Create your views here.

def home(request):
    if hasattr(request.user, 'teacher') or hasattr(request.user, 'guest'):
        deliveries = Delivery.objects.filter(Q(workgroup__advisor=request.user) | Q(workgroup__guest=request.user)).order_by('-submission_date')

        allocations = Allocation.objects.filter(evaluators__in=[request.user])

        return render(request, 'home.html', {'deliveries': deliveries, 'allocations': allocations})

    elif hasattr(request.user, 'student'):
        discipline = Discipline.objects.filter(users__in=[request.user]).order_by('-end_date').first()

        if discipline:
            activities = Activity.objects.filter(discipline__id=discipline.pk)
            return render(request, 'home.html', {'activities': activities, 'discipline_id': discipline.pk})

    return render(request, 'home.html')

def logout_app(request):
    logout(request)
    return redirect('home')

def change_password(request):
    change_password_form = PasswordChangeForm(request.user, request.POST or None)

    if request.method == 'POST':
        if change_password_form.is_valid():
            user = change_password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Corrija as informações inseridas!')

    return render(request, 'change_password.html', { 'change_password_form': change_password_form })
