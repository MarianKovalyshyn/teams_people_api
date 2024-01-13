from rest_framework import viewsets

from teams_people_service.models import Person, Team
from teams_people_service.serializers import (
    PersonSerializer,
    PersonListSerializer,
    PersonDetailSerializer,
    TeamSerializer,
    TeamListSerializer,
    TeamDetailSerializer
)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonListSerializer
        if self.action == 'retrieve':
            return PersonDetailSerializer
        return self.serializer_class


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        if self.action == 'retrieve':
            return TeamDetailSerializer
        return self.serializer_class
