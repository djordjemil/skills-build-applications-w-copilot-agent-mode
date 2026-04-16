from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users without team first
        users = []
        for email, username, team in [
            ('ironman@marvel.com', 'ironman', marvel),
            ('captain@marvel.com', 'captain', marvel),
            ('batman@dc.com', 'batman', dc),
            ('superman@dc.com', 'superman', dc),
        ]:
            user = User(email=email, username=username)
            user.set_password('password')
            user.save()
            # Update team using raw update
            User.objects.filter(pk=user.pk).update(team_id=team.pk)
            user.refresh_from_db()
            users.append(user)

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20)
        Activity.objects.create(user=users[2], type='swim', duration=45, distance=2)
        Activity.objects.create(user=users[3], type='run', duration=25, distance=4)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Run and cycle mix', duration=45)
        Workout.objects.create(name='Strength', description='Pushups and squats', duration=30)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=80)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
