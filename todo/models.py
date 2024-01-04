from django.db import models
import datetime
from django.utils import timezone
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True,  null=True)
    reg_date= models.DateField(default=timezone.now, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title  