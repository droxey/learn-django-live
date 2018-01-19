from django.db import models

# Create your models here.
class Task(models.Model):
  complete = models.BooleanField(default=False)
  created = models.DateField(auto_now=True)
  completed = models.DateField(blank=True, null=True)
  description = models.CharField(max_length=500, blank=False, null=False)
  number = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.description
