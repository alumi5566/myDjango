"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from rtChat import routing

# Below code in your asgi.py for making it work with sockets and creating routings.
#
# We usually work with wsgi.py which is in the standard Django without any asynchronous support.
# But here we are using asynchronous channels. So we have to define the routings in a different way than URLs.
#
# For HTTP we define that use the normal application which we were already using,
# now we have introduced another protocol, that is ws ( WebSocket ) for which you have to route.
#
# The ProtocolTypeRouter creates routes for different types of protocols used in the application.
# AuthMiddlewareStack authenticates the routes and instances for the Authentication and URLRouter routes the ws ( WebSocket connections ).
# The protocol for WebSockets is known as “ws”. For different requests we use HTTP.
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() ,
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)
