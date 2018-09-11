from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Activity
from .forms import  ActivitiesForm

@login_required
def activities_list(request, discipline_id):
    activities = Activity.objects.filter(discipline__id=discipline_id)
    return render(request, 'activities.html', {'activities': activities, 'discipline_id': discipline_id})

@login_required
def activities_new(request, discipline_id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    activities_form = ActivitiesForm(request.POST or None)

    if activities_form.is_valid():
        new_activity = activities_form.save(commit=False)
        new_activity.discipline_id = discipline_id
        new_activity.save()

        return redirect('activities_list', discipline_id=discipline_id)
    return render(request, 'activity_form.html', {'activities_form': activities_form, 'discipline_id': discipline_id})

@login_required
def activities_show(request, discipline_id, id):
    activity = get_object_or_404(Activity, pk=id)

    return render(request, 'activity_show.html', {'activity': activity, 'discipline_id': discipline_id})

@login_required
def activities_update(request, discipline_id, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    activity = get_object_or_404(Activity, pk=id)
    activities_form = ActivitiesForm(request.POST or None, request.FILES or None, instance=activity)

    if activities_form.is_valid():
        activities_form.save()
        return redirect('activities_list', discipline_id=discipline_id)

    return render(request, 'activity_form.html', {'activities_form': activities_form, 'discipline_id': discipline_id})

@login_required
def activities_delete(request, discipline_id, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    activity = get_object_or_404(Activity, pk=id)

    if request.method == 'POST':
        activity.delete()
        return redirect('activities_list', discipline_id=discipline_id)

    return render(request, 'activity_delete_confirm.html', {'activity': activity, 'discipline_id': discipline_id})
