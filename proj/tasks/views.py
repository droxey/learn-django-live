from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task

"""
The homepage with task list.
"""
def home(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/home.html', {
    'name': 'dani',
    'tasks': tasks
  })

"""
Page to add a task.
"""
def add_task(request):
  html_string = '<h1>Add Task</h1>'
  return HttpResponse(html_string)


"""
Endpoint to complete tasks.
"""
def complete_task(request):
  html_string = '<h1>Complete Task</h1>'
  return HttpResponse(html_string)
