# user/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SoceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        self.room_name = "car"
        self.room_group_name = "car_group"  # Can be used for broadcasting to all connected clients
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Disconnect the WebSocket connection
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
