from .models import Run
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ['id','name','category']