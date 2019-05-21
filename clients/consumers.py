# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Bergabung dengan group chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Meninggalkan group chat
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Mendapatkan pesan group chat
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Kirim pesan ke group chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Menerima pesan dari group chat
    async def chat_message(self, event):
        message = event['message']

        # mengirim pesan ke websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))