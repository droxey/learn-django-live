from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        exclude = ()
