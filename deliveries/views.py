from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Delivery
from .forms import StudentsDeliveriesForm
from workgroups.models import Workgroup

@login_required
def deliveries_list(request, activity_id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    deliveries = Delivery.objects.filter(activity__id=activity_id)
    return render(request, 'deliveries.html', {'deliveries': deliveries, 'activity_id': activity_id})

@login_required
def deliveries_list_by_workgroup(request, activity_id, workgroup_id):
    deliveries = Delivery.objects.filter(activity__id=activity_id, workgroup__id=workgroup_id)
    return render(request, 'deliveries_list_by_workgroup.html', {'deliveries': deliveries, 'activity_id': activity_id, 'workgroup_id': workgroup_id})

@login_required
def students_deliveries_new(request, activity_id, workgroup_id):
    workgroup = get_object_or_404(Workgroup, pk=workgroup_id)

    if not request.user in workgroup.students.all():
        return render(request, 'statuses/401.html')

    students_deliveries_form = StudentsDeliveriesForm(request.POST or None, request.FILES or None)

    if students_deliveries_form.is_valid():
        new_delivery = students_deliveries_form.save(commit=False)
        new_delivery.activity_id = activity_id
        new_delivery.workgroup_id = workgroup_id
        new_delivery.save()

        return redirect('deliveries_list_by_workgroup', activity_id=activity_id, workgroup_id=workgroup_id)
    return render(request, 'student_delivery_form.html', {'students_deliveries_form': students_deliveries_form, 'activity_id': activity_id, 'workgroup_id': workgroup_id})
