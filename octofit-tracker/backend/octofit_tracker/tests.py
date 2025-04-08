from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        team = Team.objects.create(name="Test Team")
        team.members.add(user)
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, type="Running", duration=30, calories_burned=300, date="2025-04-08")
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, points=100, rank=1)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session", duration=60, calories_burned=200)
        self.assertEqual(workout.name, "Morning Yoga")
