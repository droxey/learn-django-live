from django.shortcuts import render, Http404
from django.http import HttpResponse
from tasks.models import Task

from django.views.generic import ListView


"""
The homepage with task list.
"""
class TaskListView(ListView):
  model = Task
  template_name = 'tasks/home.html'
  context_object_name = 'tasks'


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
  try:
    task = Task.objects.get(id=task_id)
  except Task.DoesNotExist:
    raise Http404('Task does not exist.')
  # task = get_object_or_404(Task, task_id)
  return render(request, 'tasks/view.html', {
      'name': 'dani',
      'task': task
  })


