from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Allocation
from .forms import  AllocationsForm
from .utils import send_new_allocation_mail

@login_required
def allocations_list(request, event_id):
    if request.user.is_superuser:
        allocations = Allocation.objects.filter(event__id=event_id)
    else:
        allocations = Allocation.objects.filter(event__id=event_id, evaluators__in=[request.user])
    return render(request, 'allocations.html', {'allocations': allocations, 'event_id': event_id})

@login_required
def allocations_new(request, event_id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    allocations_form = AllocationsForm(request.POST or None)

    if allocations_form.is_valid():
        new_allocation = allocations_form.save(commit=False)

        previous_allocations = Allocation.objects.filter(event__id=event_id, selected_room=new_allocation.selected_room)
        for allocation in previous_allocations:
            before_event = new_allocation.start_time < allocation.start_time and new_allocation.end_time < allocation.start_time
            after_event = new_allocation.start_time > allocation.end_time and new_allocation.end_time > allocation.end_time
            if not(before_event or after_event):
                return render(request, 'allocation_form.html', {'allocations_form': allocations_form, 'event_id': event_id})

        new_allocation.event_id = event_id
        new_allocation.save()
        allocations_form.save_m2m()

        return redirect('allocations_list', event_id=event_id)
    return render(request, 'allocation_form.html', {'allocations_form': allocations_form, 'event_id': event_id})

@login_required
def allocations_show(request, event_id, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    allocation = get_object_or_404(Allocation, pk=id)

    return render(request, 'allocation_show.html', {'allocation': allocation, 'event_id': event_id})

@login_required
def allocations_update(request, event_id, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    allocation = get_object_or_404(Allocation, pk=id)
    allocations_form = AllocationsForm(request.POST or None, request.FILES or None, instance=allocation)

    if allocations_form.is_valid():
        allocations_form.save()
        return redirect('allocations_list', event_id=event_id)

    return render(request, 'allocation_form.html', {'allocations_form': allocations_form, 'event_id': event_id})

@login_required
def allocations_delete(request, event_id, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    allocation = get_object_or_404(Allocation, pk=id)

    if request.method == 'POST':
        allocation.delete()
        return redirect('allocations_list', event_id=event_id)

    return render(request, 'allocation_delete_confirm.html', {'allocation': allocation, 'event_id': event_id})

@login_required
def allocations_send_info_email(request, event_id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    allocations = Allocation.objects.filter(event__id=event_id)

    for allocation in allocations:
        send_new_allocation_mail(allocation)

    return redirect('allocations_list', event_id=event_id)
