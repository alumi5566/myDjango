from django.urls import path, include
from rtChat.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
# routing.py: This will route the WebSocket connections to the consumers.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
