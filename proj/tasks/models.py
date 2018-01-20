from django.db import models

# Create your models here.
class Task(models.Model):
  complete = models.BooleanField(default=False)
  created = models.DateField(auto_now_add=True)
  completed = models.DateField(blank=True, null=True)
  description = models.CharField(max_length=500, blank=False, null=False)
  number = models.IntegerField(blank=True, null=True)
  modified = models.DateField(auto_now=True)

  def __str__(self):
    return self.description

  def save(self, *args, **kwargs):
    if not self.id:
      self.number = 1
    else:
      self.number = 99
    return super(Task, self).save(*args, **kwargs)
