# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from myapp.models import YourModel

class MyAsyncJsonWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print('payload received')

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process the data and save it to the database
        instance = YourModel.objects.create(**data)
        await self.send(text_data=json.dumps({
            'message': 'Data saved successfully!',
            'data': data
        }))
