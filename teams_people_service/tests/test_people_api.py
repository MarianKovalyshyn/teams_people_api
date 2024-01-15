from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from teams_people_service.models import Person
from teams_people_service.serializers import (
    PersonSerializer, PersonListSerializer, PersonDetailSerializer
)

PERSON_LIST_URL = reverse('teams_people_service:person-list')


def sample_person(num: int) -> Person:
    person = Person.objects.create(
            name=f'Person {num}',
            surname=f'Surname {num}',
            email=f'person{num}@test.com',
            team=None
        )

    return person


class PersonApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_person_list(self):
        sample_person(1)
        sample_person(2)
        res = self.client.get(PERSON_LIST_URL)
        persons = Person.objects.all()
        serializer = PersonListSerializer(persons, many=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_get_person_detail(self):
        person = sample_person(1)
        res = self.client.get(reverse(
            'teams_people_service:person-detail', args=[person.id]
        ))
        serializer = PersonDetailSerializer(person)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_create_person(self):
        payload = {
            'name': 'Person 1',
            'surname': 'Surname 1',
            'email': 'person1@test.com',
            'team': ''
        }
        res = self.client.post(PERSON_LIST_URL, payload)
        person = Person.objects.get(id=res.data['id'])
        serializer = PersonSerializer(person)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data, serializer.data)
