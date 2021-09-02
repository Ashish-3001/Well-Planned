from django.db import models
from my_app.models import DairyCatagory

class Entry(models.Model):
    catagory = models.ForeignKey(DairyCatagory, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'