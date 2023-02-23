from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("polls/", views.list, name="polls"),
    path("hello/", views.hello, name="hello"),
]
