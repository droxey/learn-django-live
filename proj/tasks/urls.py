from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^list/$', views.home, name='task-list'),
  url(r'^add/$', views.add_task, name='add-task'),
  url(r'^complete/$', views.complete_task, name='complete-task'),
]
