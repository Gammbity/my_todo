from rest_framework import serializers
from .models import TodoModel, User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    class Meta:
        model = TodoModel
        fields = '__all__'

    @receiver(pre_save, sender=TodoModel)
    def check_when(sender, instance, **kwargs):
        when = str(instance.when)
        when_date = datetime.datetime.strptime(when, '%Y-%m-%d %H:%M:%S%z').date()
        todo = TodoModel.objects.all()
        if when_date > datetime.datetime.now().date():
            todo.when = instance.when
        else:
            e = f"Ushbu {instance.when} yaroqsiz!"
            raise serializers.ValidationError({
                'data': e
            })
    
class TodoUpdateSerialezer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['is_did']