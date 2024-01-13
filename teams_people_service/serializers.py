from rest_framework import serializers

from teams_people_service.models import Person, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email', 'team')


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname')


class PersonDetailSerializer(PersonSerializer):
    team = serializers.StringRelatedField()
