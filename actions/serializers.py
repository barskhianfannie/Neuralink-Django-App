# from rest_framework import serializers
from .models import Action
from django.contrib import admin
from rest_framework import serializers




class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "task", "completed", "timestamp", "updated", "device","user", 'data']
        style={'base_template': 'rest_framework/inp.html'}
