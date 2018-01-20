from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^view/(?P<task_id>[0-9]+)/$', views.view_task, name='view-task'),
  url(r'^list/$', views.TaskListView.as_view(), name='task-list'),
  url(r'^add/$', views.add_task, name='add-task'),
  url(r'^complete/$', views.complete_task, name='complete-task'),
]
