from django.urls import path
from . import views
from .consumers import BingoConsumer
from django.conf import settings
from django.conf.urls.static import static
app_name = 'games'

urlpatterns = [
    path('send-numbers/', BingoConsumer.send_numbers, name='send_numbers'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('Bingo/', views.bingo, name='Bingo'),
    path('BingoGame/', views.BingoGame, name='BingoGame'),
    path('MusicalChair/', views.MusicalChairs, name='MusicalChair'),
    path('SpinTheWheel/', views.SpinTheWheel, name='SpinTheWheel'),
    path('Pinata/', views.PinataGame, name='Pinata'),
    path('FindImposter/', views.FindImposter, name='FindImposter'),
    path('Monkey/', views.MonkeyGame, name='Monkey'),
]