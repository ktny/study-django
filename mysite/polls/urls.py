from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("polls/", views.polls, name="polls"),
    path("hello/", views.hello, name="hello"),
    path("drf/", views.drf, name="drf"),
]
