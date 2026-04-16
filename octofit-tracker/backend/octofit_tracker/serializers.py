from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    def get_team(self, obj):
        return str(obj.team_id) if obj.team_id else None

    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    def get_user(self, obj):
        return str(obj.user_id)

    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    def get_user(self, obj):
        return str(obj.user_id)

    class Meta:
        model = Leaderboard
        fields = '__all__'
