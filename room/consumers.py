from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Message,Room
import json

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        await self.get_room()
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        room_id = text_data_json['room_id']
        username = text_data_json['username']
        message = text_data_json['message']

        await self.create_message(room_id,username,message)
        print("Message saved")

        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat.message', 'message': message, 'username': username}
        )
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    @sync_to_async
    def create_message(self,room,username,message):
        room_instance = Room.objects.get(id=room)
        sender = User.objects.get(username=username)
        message_instance = Message.objects.create(room=room_instance,sender=sender,content=message)

        return message_instance

    @sync_to_async
    def get_room(self):
        return Room.objects.get(id=self.room_id)
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))