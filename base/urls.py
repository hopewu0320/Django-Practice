"""studybud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#葉目錄
from django.contrib import admin
from django.urls import path,include
from . import views
'''
可改成path("room_page/<str:pk>",views.room,name='room') 還是會根據name去執行
'''
urlpatterns = [
    path("room/<str:pk>",views.room,name='room'),
    path("profile/<str:pk>",views.userProfile,name='user-profile'), 
    path("",views.home,name='home'),
    path("login/",views.loginPage,name='login'),
    path("register/",views.registerPage,name='register'),
    path("logout/",views.logoutUser,name='logout'),
    path("create-room/",views.createRoom,name='create-room'),
    path("update-room/<str:pk>/",views.updateRoom,name='update-room'),
    path("delete-room/<str:pk>/",views.deleteRoom,name='delete-room'),
    path("delete-message/<str:pk>/",views.deleteMessage,name='delete-message')
]
