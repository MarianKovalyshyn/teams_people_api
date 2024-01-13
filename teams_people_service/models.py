from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)


class Team(models.Model):
    name = models.CharField(max_length=100)
