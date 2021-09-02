from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth

from remindapp.form import reminder_form
from .models import Reminder


# Create your views here.
def index(request):
    return render(request, "home.html")

def updatereminder(request, pk):

    post = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = reminder_form(request.POST, instance=post)
        if form.is_valid():
                 post = form.save(commit=False)
                 post.save()
                 return redirect('home')
    else:
        form = reminder_form()
    return render(request, 'reminderdetails.html', {'form': form})

def add_reminder(request):
    if request.method== 'POST':
        form = reminder_form(request.POST)
        if form.is_valid():
            rem=form.save(commit=False)
            rem.user=request.user
            rem.save()
            return redirect('home')
    else:
        form = reminder_form()
    return render(request, 'reminderdetails.html', {'form': form})

def reminderview(request):
    obj = Reminder.objects.all()
    return render(request, "reminderview.html", {'reminders':obj})


def deletereminder(request, pk):
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return redirect('reminderview')
    reminder.delete()
    return redirect('reminderview')
