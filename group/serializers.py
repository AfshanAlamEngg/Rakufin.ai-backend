from rest_framework import serializers
from .models import Group
from user.serializers import UserSerializer

class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'users']
