from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
import uuid

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_rooms") 
    members = models.ManyToManyField(User,related_name="joined_rooms")

    def has_permission(self,user):
        return user==self.created_by
    
    def add_member(self,user):
        if self.has_permission(self.created_by) and user not in self.members.all():
            self.members.add(user)
    
    def remove_member(self,user):
        if self.has_permission(self.created_by) and user in self.members.all():
            self.members.remove(user)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.username