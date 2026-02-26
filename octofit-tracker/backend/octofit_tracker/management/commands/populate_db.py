from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# MODELE (minimalne, do testów)
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Usuń stare dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj zespoły
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Dodaj użytkowników
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for u in users:
            u.save()

        # Dodaj aktywności
        Activity.objects.create(user='Iron Man', type='Running', duration=30)
        Activity.objects.create(user='Batman', type='Cycling', duration=45)

        # Dodaj leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Dodaj workouty
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
