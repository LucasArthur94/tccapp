from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Delivery
from .forms import StudentsDeliveriesForm
from workgroups.models import Workgroup
from activities.models import Activity

@login_required
def deliveries_list(request, activity_id):
    if request.user.is_superuser:
        deliveries = Delivery.objects.filter(activity__id=activity_id)
    else:
        deliveries = Delivery.objects.filter(Q(workgroup__students__in=[request.user]) | Q(workgroup__advisor=request.user) | Q(workgroup__guest=request.user), activity__id=activity_id)

    activity = get_object_or_404(Activity, pk=activity_id)

    deliveries = Delivery.objects.filter(activity__id=activity_id)
    return render(request, 'deliveries.html', {'deliveries': deliveries, 'activity': activity})

@login_required
def deliveries_new(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    workgroup = Workgroup.objects.filter(students__in=[request.user]).order_by('-created_at').first()

    if not workgroup or activity.is_closed:
        return render(request, 'statuses/401.html')

    students_deliveries_form = StudentsDeliveriesForm(request.POST or None, request.FILES or None)

    if students_deliveries_form.is_valid():
        new_delivery = students_deliveries_form.save(commit=False)
        new_delivery.activity_id = activity_id
        new_delivery.workgroup_id = workgroup.pk
        new_delivery.save()

        return redirect('deliveries_list_workgroup', activity_id=activity_id, workgroup_id=workgroup.pk)
    return render(request, 'student_delivery_form.html', {'students_deliveries_form': students_deliveries_form, 'activity': activity})
