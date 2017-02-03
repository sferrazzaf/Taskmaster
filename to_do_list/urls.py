from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^todolist/$', views.todolist, name='todolist'),
        url(r'^todolist/reorder/$', views.reorder, name='reorder'),
        url(r'^todolist/togglecurrent/$', views.togglecurrent,
            name='togglecurrent'),
        url(r'^todolist/delete/([0-9]+)/$', views.deletetask, name='deletetask')
        ]
