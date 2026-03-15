from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.user, self.user)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard.team, self.team)
