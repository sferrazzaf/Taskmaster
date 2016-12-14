from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^todolist/$', views.todolist, name='todolist'),
        ]
