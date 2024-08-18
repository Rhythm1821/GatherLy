from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.user not in room.members.all():
        messages.error(request,'You are not a member of this room')
        return redirect('home')
    return render(request,'room.html',{'room':room})

@login_required
def delete_room(request,room_id):
    room=Room.objects.get(id=room_id)
    if request.user.username==room.created_by.username:
        room.delete()
        messages.success(request,'Room deleted successfully')
        return redirect('home')
    else:
        PermissionDenied('You do not have permission to delete this room')
        return redirect('home')
from django.http import JsonResponse
    
@login_required    
def search(request):
    if request.method=='POST':
        print("Searching...")
        if request.POST.get('search'):
            search = request.POST['search']
            rooms = Room.objects.filter(name__contains=search)
            return render(request,'search.html',{"rooms":rooms,"search":search})
        else:
            room_name = request.POST.get('room_name')
            uuid = request.POST.get('uuid')
            if room_name and uuid:
                try:
                    room = Room.objects.get(name=room_name)
                    if str(room.id) == uuid:
                        room.members.add(request.user)
                        return JsonResponse({'room_id': room.id})
                    else:
                        return JsonResponse({'error': 'Invalid UUID provided.'}, status=400)
                except Room.DoesNotExist:
                    return JsonResponse({'error': 'Room not found.'}, status=404)
            return JsonResponse({'error': 'Required fields are missing.'}, status=400)
    return render(request,'search.html')


@login_required
def delete_member(request,room_id,member_id):
    room = Room.objects.get(id=room_id)
    if request.user.username == room.created_by.username:
        room.members.remove(User.objects.get(id=member_id))
        messages.success(request,'Member removed successfully')
        return redirect(request.META['HTTP_REFERER'])
    messages.error(request,'You do not have permission to delete this member')
    return redirect(request.META['HTTP_REFERER'])


@login_required
def all_members(request,room_id):
    room = Room.objects.get(id=room_id)
    members = room.members.all()
    return render(request,'all_members.html',{'room':room, 'members':members})