from rest_framework import serializers
from .models import TodoModel, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
    
class TodoUpdateSerialezer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['is_did']