from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^todolist/$', views.todolist, name='todolist'),
        url(r'^todolist/reorder/$', views.reorder, name='reorder')
        ]
