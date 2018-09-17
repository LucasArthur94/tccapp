from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Delivery
from .forms import StudentsDeliveriesForm, AdvisorsGuestsDeliveriesForm
from .utils import send_new_delivery_mail
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
    return render(request, 'deliveries.html', {'deliveries': deliveries, 'activity': activity, 'discipline_id': activity.discipline.pk})

@login_required
def deliveries_show(request, activity_id, id):
    activity = get_object_or_404(Activity, pk=activity_id)

    delivery = get_object_or_404(Delivery, pk=id)

    return render(request, 'delivery_show.html', {'delivery': delivery, 'activity': activity})

@login_required
def deliveries_new(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    workgroup = Workgroup.objects.filter(students__in=[request.user]).order_by('-created_at').first()

    if not workgroup or activity.is_closed():
        return render(request, 'statuses/401.html')

    students_deliveries_form = StudentsDeliveriesForm(activity, request.POST or None, request.FILES or None)

    if students_deliveries_form.is_valid():
        new_delivery = students_deliveries_form.save(commit=False)
        new_delivery.author_id = request.user.pk
        new_delivery.activity_id = activity_id
        new_delivery.workgroup_id = workgroup.pk
        new_delivery.save()

        send_new_delivery_mail(new_delivery)

        return redirect('deliveries_list', activity_id=activity_id)
    return render(request, 'student_delivery_form.html', {'students_deliveries_form': students_deliveries_form, 'activity': activity})

@login_required
def deliveries_update(request, activity_id, id):
    delivery = get_object_or_404(Delivery, pk=id)

    activity = get_object_or_404(Activity, pk=activity_id)

    workgroup = Workgroup.objects.filter(students__in=[request.user]).order_by('-created_at').first()

    if not workgroup or activity.is_closed() or delivery.is_avaliated:
        return render(request, 'statuses/401.html')

    students_deliveries_form = StudentsDeliveriesForm(activity, request.POST or None, request.FILES or None, instance=delivery)

    if students_deliveries_form.is_valid():
        new_delivery = students_deliveries_form.save(commit=False)
        new_delivery.author_id = request.user.pk
        new_delivery.save()

        return redirect('deliveries_list', activity_id=activity_id)
    return render(request, 'student_delivery_form.html', {'students_deliveries_form': students_deliveries_form, 'activity': activity})

@login_required
def deliveries_review(request, activity_id, id):
    delivery = get_object_or_404(Delivery, pk=id)

    activity = get_object_or_404(Activity, pk=activity_id)

    workgroup = Workgroup.objects.filter(Q(guest=request.user) | Q(advisor=request.user)).order_by('-created_at').first()

    if not workgroup or (delivery.is_avaliated_by_advisor and not hasattr(request.user, 'teacher')):
        return render(request, 'statuses/401.html')

    advisors_guests_deliveries_form = AdvisorsGuestsDeliveriesForm(request.POST or None, instance=delivery)

    if advisors_guests_deliveries_form.is_valid():
        new_delivery = advisors_guests_deliveries_form.save(commit=False)
        if hasattr(request.user, 'guest'):
            new_delivery.status = 'AGS'
        elif hasattr(request.user, 'teacher'):
            new_delivery.status = 'AAD'
        new_delivery.save()

        return redirect('deliveries_list', activity_id=activity_id)
    return render(request, 'advisor_guest_delivery_form.html', {'advisors_guests_deliveries_form': advisors_guests_deliveries_form, 'activity': activity})

@login_required
def deliveries_delete(request, activity_id, id):
    delivery = get_object_or_404(Delivery, pk=id)

    activity = get_object_or_404(Activity, pk=activity_id)

    workgroup = Workgroup.objects.filter(students__in=[request.user]).order_by('-created_at').first()

    if not workgroup or activity.is_closed() or delivery.is_avaliated:
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        delivery.delete()
        return redirect('deliveries_list', activity_id=activity_id)

    return render(request, 'delivery_delete_confirm.html', {'delivery': delivery})
