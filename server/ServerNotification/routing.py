from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from user.consumers import soce

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('car/', soce.as_asgi()),  # Ensure the consumer is set up correctly
    ]),
})
