from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room,Topic
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import RoomForm
# Create your views here.
rooms=[
    {'id':1,'name':'Let s learn Python!'},
    {'id':2,'name':'Design with me'},
    {'id':3,'name':'Fronted developers'}
]
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username Or Password not exist")
    context= {}
    return render(request, 'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('home')
def home(request):
    print("HOME")
    q = request.GET.get('q') if request.GET.get('q') != None else '' #找url的"q"字串後的名稱
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q)  |
                                Q(description__icontains=q) ) 
    topics = Topic.objects.all()
    room_count = rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/home.html',context)
def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()      #存在資料庫(代表有這個room的所有資訊)
            return redirect('home')  #使用urls.py的"name"
    context={'form':form}
    return render(request,'base/room_form.html',context)
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  #form的起始值是這個room的資訊
    if request.method == 'POST':
        form=RoomForm(request.POST,instance=room) #告訴她哪個room要更新(instance的部分)
        if form.is_valid():
            form.save()      #存在資料庫(代表有這個room的所有資訊)
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    context={'obj':room}
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',context)