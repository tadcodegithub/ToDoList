from rest_framework import serializers
from .models import Task
#to feech all data
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
