from django.shortcuts import render, Http404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from tasks.forms import TaskForm

from django.views.generic import ListView
from django.urls import reverse


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
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      new_task = Task(description=request.POST.get('description', ''))
      new_task.save()
      return HttpResponseRedirect(reverse('task-list'))
  form = TaskForm()
  return render(request, 'tasks/add.html', {
    'form': form
  })


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


