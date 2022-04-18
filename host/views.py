from pstats import Stats
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Device
from actions.models import Action

ALLOWED_HOSTS = settings.ALLOWED_HOSTS




def home_view(request, *args, **kwargs):
    devices = Device.newmanager.all()
    actions = Action.newmanager.all()
    return render(request, 'host/index.html', {'devices': devices, 'actions': actions}, status=200)




def device_list_view(request, *args, **kwargs):
    """
    REST API
    Return JSON for React, etc.
    """
    qs = Device.objects.all()
    device_list = [{"id": x.id, "name":x.deviceName, "image":x.image, 'manufDate':x.dateManufactured, 'expDate':x.dateExpires, 'data':x.data } for x in qs]
    data={"response": device_list}
    return JsonResponse(data)


# def profile_view(request, *args, **kwargs):
#     devices = Device.newmanager.all()
#     return render(request, 'host/index.html', {'devices': devices}, status=200)