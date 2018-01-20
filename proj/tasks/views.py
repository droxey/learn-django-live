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


"""
Page that will allow us to view a single task by ID.
"""
def view_task(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/view.html', {
      'name': 'dani',
      'task': task
  })
