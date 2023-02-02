from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room,Topic,Message
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RoomForm
# Create your views here.
rooms=[
    {'id':1,'name':'Let s learn Python!'},
    {'id':2,'name':'Design with me'},
    {'id':3,'name':'Fronted developers'}
]
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated: #避免輸入login page user時候重複登入
        return redirect('home')
    if request.method == 'POST':
        username=request.POST.get('username').lower()
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
    context= {'page':page}
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
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body') #前端room.html送過來的Send Message
        )
        room.participants.add(request.user)  #此user會被加入到many to many的系統
        return redirect('room',pk=room.id)
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)

@login_required(login_url='login')  #當還沒登入的時候鼓勵人登入
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()      #存在資料庫(代表有這個room的所有資訊)
            return redirect('home')  #使用urls.py的"name"
    context={'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login') #確保有user登入下才能update
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  #form的起始值是這個room的資訊
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")
    if request.method == 'POST':
        form=RoomForm(request.POST,instance=room) #告訴她哪個room要更新(instance的部分)
        if form.is_valid():
            form.save()      #存在資料庫(代表有這個room的所有資訊)
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
@login_required(login_url='login') #確保有user登入下才能刪除房間
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    context={'obj':room} #因為會delete room或者message所以用'obj'
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',context)

@login_required(login_url='login') #確保有user登入下才能刪除房間
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    context={'obj':message}  #因為會delete room或者message所以用'obj'
    if request.user != message.user:
        return HttpResponse("You are not allowed here!!")
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #freeze it 要馬上使用 user資訊
            user.username = user.username.lower()
            user.save()
            login(request,user) #註冊完馬上登入
            return redirect('home')
        else:
            messages.error(request,"An error occurred while registration")
    context={'form':form}
    return render(request, 'base/login_register.html',context)