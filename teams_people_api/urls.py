from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teams_people_service.urls', namespace='teams_people_service')),
]
