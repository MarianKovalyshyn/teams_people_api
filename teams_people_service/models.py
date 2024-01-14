from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    team = models.ForeignKey(
        'Team', on_delete=models.SET_NULL, null=True, related_name='persons'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
