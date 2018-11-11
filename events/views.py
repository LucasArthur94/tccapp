from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Event
from .forms import  EventsForm

@login_required
def events_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    events = Event.objects.all().order_by('-end_time')
    return render(request, 'events.html', {'events': events})

@login_required
def events_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    events_form = EventsForm(request.POST or None)

    if events_form.is_valid():
        events_form.save()

        return redirect('events_list')
    return render(request, 'event_form.html', {'events_form': events_form})

@login_required
def events_show(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    event = get_object_or_404(Event, pk=id)

    return render(request, 'event_show.html', {'event': event})

@login_required
def events_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    event = get_object_or_404(Event, pk=id)
    events_form = EventsForm(request.POST or None, request.FILES or None, instance=event)

    if events_form.is_valid():
        events_form.save()
        return redirect('events_list')

    return render(request, 'event_form.html', {'events_form': events_form})

@login_required
def events_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    event = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        event.delete()
        return redirect('events_list')

    return render(request, 'event_delete_confirm.html', {'event': event})
