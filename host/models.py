from django.db import models
from django.db import models
from django import utils, forms
from django.conf import settings
import datetime as dt
from django.urls import reverse

User=settings.AUTH_USER_MODEL

# Create your models here.
class Device(models.Model):


    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()


    deviceName = models.TextField(blank=True, null=True)
    img = models.FileField(upload_to='static/images/', blank=True)
    dateManufactured =  models.DateTimeField('Manufactured Date',default=None,null=True)
    dateExpires =  models.DateTimeField('Expiration Date',default=None,null=True)
    slug = models.SlugField(max_length=250, blank=True, default='device26178')
    user = models.ManyToManyField(User,  default=None)
    data = models.TextField(max_length=500000,null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager


    def get_absolute_url(self):
        return reverse('host:vote_single', args=[self.slug])