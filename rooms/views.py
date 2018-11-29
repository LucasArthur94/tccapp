from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room
from .forms import RoomsForm

@login_required
def rooms_list(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def rooms_new(request):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    rooms_form = RoomsForm(request.POST or None)

    if rooms_form.is_valid():
        rooms_form.save()
        messages.success(request, 'Sala salva com sucesso!')
        return redirect('rooms_list')
    return render(request, 'room_form.html', {'rooms_form': rooms_form})

@login_required
def rooms_show(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    room = get_object_or_404(Room, pk=id)

    return render(request, 'room_show.html', {'room': room})

@login_required
def rooms_update(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    room = get_object_or_404(Room, pk=id)
    rooms_form = RoomsForm(request.POST or None, request.FILES or None, instance=room)

    if rooms_form.is_valid():
        rooms_form.save()
        messages.success(request, 'Sala alterada com sucesso!')
        return redirect('rooms_list')
    return render(request, 'room_form.html', {'rooms_form': rooms_form})

@login_required
def rooms_delete(request, id):
    if not request.user.is_superuser:
        return render(request, 'statuses/401.html')

    room = get_object_or_404(Room, pk=id)

    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Sala excluída com sucesso!')
        return redirect('rooms_list')
    return render(request, 'room_delete_confirm.html', {'room': room})
