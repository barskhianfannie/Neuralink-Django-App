from django.shortcuts import render

# Create your views here.

from .models import Action


from rest_framework import viewsets

from .serializers import ActionSerializer
from .models import Action
 

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


