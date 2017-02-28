from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^todolist/([0-9]+)/$', views.todolist, name='todolist'),
        url(r'^todolist/([0-9]+)/reorder/$', views.reorder, name='reorder'),
        url(r'^todolist/([0-9]+)/togglecurrent/$', views.togglecurrent,
            name='togglecurrent'),
        url(r'^todolist/([0-9]+)/delete/([0-9]+)/$', views.deletetask,
        name='deletetask'),
        url(r'^todolist/[0-9]+/pausetask/([0-9]+)/$', views.pausetask,
        name='pausetask'),
        url(r'^todolist/[0-9]+/finishtask/([0-9]+)/$', views.finishtask,
        name='finishtask')
        ]
