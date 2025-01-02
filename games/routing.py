from django.urls import path
from .consumers import BingoConsumer

websocket_urlpatterns = [
    path('ws/bingo/', BingoConsumer.as_asgi()),
]
