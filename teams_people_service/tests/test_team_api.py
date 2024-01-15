from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from teams_people_service.models import Team
from teams_people_service.serializers import (
    TeamSerializer, TeamListSerializer, TeamDetailSerializer
)

TEAM_LIST_URL = reverse('teams_people_service:team-list')


class TeamApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_team_list(self):
        Team.objects.create(name='Team 1')
        Team.objects.create(name='Team 2')

        res = self.client.get(TEAM_LIST_URL)
        teams = Team.objects.all()
        serializer = TeamListSerializer(teams, many=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_get_team_detail(self):
        team = Team.objects.create(name='Team 1')
        res = self.client.get(reverse(
            'teams_people_service:team-detail', args=[team.id]
        ))
        serializer = TeamDetailSerializer(team)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_create_team(self):
        payload = {'name': 'Team 1'}
        res = self.client.post(TEAM_LIST_URL, payload)
        team = Team.objects.get(id=res.data['id'])
        serializer = TeamSerializer(team)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data, serializer.data)
