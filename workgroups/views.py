from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Workgroup
from .forms import  WorkgroupsForm
from .utils import send_new_workgroup_mail

# Create your views here.

@login_required
def workgroups_list(request):
    if request.user.is_superuser:
        workgroups = Workgroup.objects.all()
    else:
        workgroups = Workgroup.objects.filter(Q(students__in=[request.user]) | Q(advisor=request.user) | Q(guest=request.user)).distinct()
    return render(request, 'workgroups.html', {'workgroups': workgroups})

@login_required
def workgroups_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    workgroups_form = WorkgroupsForm(request.POST or None)

    if workgroups_form.is_valid():
        workgroup = workgroups_form.save()
        send_new_workgroup_mail(workgroup)

        return redirect('workgroups_list')
    return render(request, 'workgroup_form.html', {'workgroups_form': workgroups_form})

@login_required
def workgroups_show(request, id):
    workgroup = get_object_or_404(Workgroup, pk=id)

    if not request.user.is_superuser and not (request.user in workgroup.students.all() or request.user == workgroup.guest or request.user == workgroup.advisor):
        return render(request, 'statuses/401.html')


    return render(request, 'workgroup_show.html', {'workgroup': workgroup})

@login_required
def workgroups_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    workgroup = get_object_or_404(Workgroup, pk=id)
    workgroups_form = WorkgroupsForm(request.POST or None, request.FILES or None, instance=workgroup)

    if workgroups_form.is_valid():
        workgroups_form.save()
        return redirect('workgroups_list')

    return render(request, 'workgroup_form.html', {'workgroups_form': workgroups_form})

@login_required
def workgroups_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    workgroup = get_object_or_404(Workgroup, pk=id)

    if request.method == 'POST':
        workgroup.delete()
        return redirect('workgroups_list')

    return render(request, 'workgroup_delete_confirm.html', {'workgroup': workgroup})

@login_required
def workgroups_confirm_participation(request, id):
    workgroup = get_object_or_404(Workgroup, pk=id)

    if not request.user == workgroup.advisor and not request.user == workgroup.guest:
        return render(request, 'statuses/401.html')

    if request.method == 'POST':
        if request.user == workgroup.advisor:
            workgroup.advisor_validated_participation = True
            workgroup.save()
        elif request.user == workgroup.guest:
            workgroup.guest_validated_participation = True
            workgroup.save()
        return redirect('workgroups_list')

    return render(request, 'workgroup_confirm_participation.html', {'workgroup': workgroup})
