from django.urls import path
from . import consumers

# Define WebSocket URI patterns
websocket_uri = [
   # path("ws/jws/", consumers.MyJsonWebsocketConsumer.as_asgi()),
    path("ws/async/", consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]
