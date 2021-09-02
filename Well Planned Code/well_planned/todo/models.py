from django.db import models
from my_app.models import TodoListCatagory

class Todo(models.Model):
    catagory = models.ForeignKey(TodoListCatagory, on_delete=models.CASCADE)
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text