from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users
        ironman = app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = app_models.User.objects.create(name='Captain America', email='captain@marvel.com', team=marvel)
        batman = app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = app_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='Run', duration=30)
        app_models.Activity.objects.create(user=captain, type='Swim', duration=45)
        app_models.Activity.objects.create(user=batman, type='Cycle', duration=60)
        app_models.Activity.objects.create(user=superman, type='Run', duration=50)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all')
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
