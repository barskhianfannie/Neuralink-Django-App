from django.contrib import admin
from django.urls import path, include

app_name = 'host'
from accounts import views as a_views
from actions import views as act_views
from host import views as h_views


urlpatterns = [
    path('', h_views.home_view, name='homepage')

]