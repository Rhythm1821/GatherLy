from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
from room.models import Room

def index(request):
    if request.user.is_authenticated:
        rooms = request.user.joined_rooms.all()  # Room.objects.filter(members=request.user) both works
        return render(request, 'index.html',{'rooms':rooms})
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('/login/')
    else:
        return render(request,'login.html')

def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    return render(request,'register.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')