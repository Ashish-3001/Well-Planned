from django.db import models
from django.conf import settings

import _datetime
# Create your models here.

class Reminder(models.Model):
    message = models.CharField(max_length=100)
    current_date = models.DateTimeField(default=_datetime.datetime.now())
    reminder_date = models.DateTimeField(default=_datetime.datetime.now())

    def __str__(self):
        return self.message