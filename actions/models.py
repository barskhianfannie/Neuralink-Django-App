from statistics import mode
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from host.models import Device

class Action(models.Model):


    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
    task = models.TextField(max_length = 500)
    timestamp = models.DateTimeField('created',default=None,null=True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField('Update Date',default=None,null=True)
    device = models.OneToOneField(Device, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    data = models.TextField(max_length = 500,null=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def __str__(self):
        return self.task