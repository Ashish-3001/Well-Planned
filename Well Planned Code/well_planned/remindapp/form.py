from django import forms
from .models import Reminder


class reminder_form(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = '__all__'
        exclude = ('user',)
