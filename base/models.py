from django.db import models
from django.db.models.deletion import CASCADE,SET_NULL
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True) #ROOM裡面有很多個USER提供選擇
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True) #父刪除子的資料還留著 #同一個TOPIC可以有很多個ROOM
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)   #每次save的時候會更新時間戳記
    created = models.DateTimeField(auto_now_add=True) #建造物件的時候的時間戳記
    def __str__(self):
        return self.name  #stair=Room(name="樓梯") print(stair) output:樓梯

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  #代表父親為Room 有很多Message(小孩)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)  #代表父親為Room 有很多Message(小孩)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)   #每次save的時候會更新時間戳記
    created = models.DateTimeField(auto_now_add=True) #建造物件的時候的時間戳記
    def __str__(self):
        return self.body[:50]