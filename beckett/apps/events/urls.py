from django.conf.urls import include, url
from django.contrib import admin
from beckett.apps.events import views
from beckett.apps.events.views import chronology

urlpatterns = [
    url(r'^chronology$', chronology, name="chronology"),
]