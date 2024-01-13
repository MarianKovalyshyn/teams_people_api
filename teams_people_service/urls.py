from django.urls import include, path
from rest_framework import routers

from teams_people_service import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'teams', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'teams_people_service'
