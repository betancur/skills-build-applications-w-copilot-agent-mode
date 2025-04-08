from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models

class Team(models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = djongo_models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Leaderboard(models.Model):
    _id = djongo_models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"

class Workout(models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.name
