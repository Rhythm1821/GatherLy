from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .models import Room
from .forms import RoomForm

@login_required
def create_room(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.created_by=request.user
            form.save()
            room.members.add(request.user)
            return redirect('home')
    else:
        return render(request,'create_room.html',{'form':form})

@login_required    
def room(request,room_id):
    room=Room.objects.get(id=room_id)
    return render(request,'room.html',{'room':room})

@login_required
def delete_room(request,room_id):
    room=Room.objects.get(id=room_id)
    print(room)
    if request.user.username==room.created_by.username:
        room.delete()
        messages.success(request,'Room deleted successfully')
        return redirect('home')
    else:
        PermissionDenied('You do not have permission to delete this room')
        return redirect('home')
    
@login_required    
def search(request):
    if request.method=='POST':
        search = request.POST['search']
        rooms = Room.objects.filter(name__contains=search)
        return render(request,'search.html',{"rooms":rooms,"search":search})
    return render(request,'search.html')


@login_required
def join_room(request, room_name, room_id):
    try:
        original_room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return redirect('home')

    if original_room.name != room_name:
        return redirect('home')
    
    original_room.members.add(request.user)
    room=Room.objects.get(id=room_id)
    return render(request,'room.html',{'room':room})


@login_required
def delete_member(request,room_id):
    room = Room.objects.get(id=room_id)
    pass

@login_required
def all_members(request,room_id):
    room = Room.objects.get(id=room_id)
    members = room.members.all()
    return render(request,'all_members.html',{'room':room, 'members':members})