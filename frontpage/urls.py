from django.urls import path
from frontpage import views

app_name = 'frontpage'
urlpatterns = [
    path('About/', views.about, name='About'),
    path('Login/', views.login, name='Login'),
    path('', views.index, name='index'),
    
]
