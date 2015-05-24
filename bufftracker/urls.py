from django.conf.urls import patterns, url
from bufftracker import views

urlpatterns = patterns('', url(r"^$", views.index, name="index"), )
