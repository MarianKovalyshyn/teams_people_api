from rest_framework import viewsets

from teams_people_service.models import Person, Team
from teams_people_service.serializers import PersonSerializer, TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
