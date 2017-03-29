from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^todolist/([0-9]+)/$', views.todolist, name='todolist'),
        url(r'^todolist/([0-9]+)/reports/$', views.reports, name='reports'),
        url(r'^todolist/([0-9]+)/reorder/$', views.reorder, name='reorder'),
        url(r'^todolist/[0-9]+/delete/([0-9]+)/$', views.deletetask,
        name='deletetask'),
        url(r'^todolist/[0-9]+/updatetask/$', views.updatetask,
            name='updatetask')
        ]
