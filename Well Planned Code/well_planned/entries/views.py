from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from my_app.models import DairyCatagory

cid = 0

def index(request,c_id):
    global  cid
    cid = c_id

    entries = Entry.objects.filter(catagory = int(cid)).order_by('-date_posted')

    context = {'entries' : entries,'id': cid}

    return render(request, 'entries/index.html', context)

def addd(request,c_id):

    catagory = DairyCatagory.objects.get(id = int(cid))
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            new = Entry(text=request.POST['text'], catagory = catagory)
            new.save()
            return redirect('/dairyList/'+cid)
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)