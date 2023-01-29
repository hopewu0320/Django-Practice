from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=2000)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)   #每次save的時候會更新時間戳記
    created = models.DateTimeField(auto_now_add=True) #建造物件的時候的時間戳記
    def __str__(self):
        return self.name  #stair=Room(name="樓梯") print(stair) output:樓梯

class Message(models.Model):
    room = models.ForeignKey(Room,ondelete=models.CASCADE)  #代表父親為Room 有很多Message(小孩)
    body = models.TextField()