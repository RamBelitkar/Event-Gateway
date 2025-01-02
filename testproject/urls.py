from django.contrib import admin
from django.urls import path, include
from frontpage.views import redirectpage  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/', redirectpage, name='redirectpage'),  # Ensure this is defined only once
    path('', include('frontpage.urls')),
    path('games/', include('games.urls')),
]
