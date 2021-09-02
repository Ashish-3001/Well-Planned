from my_app.models import TodoListCatagory
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm
 
cid = 0

def index(request,c_id):
    global cid
    cid = c_id
    
    todo_list = Todo.objects.filter(catagory = int(cid)).order_by('id')
    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    catagory = TodoListCatagory.objects.get(id = int(cid))
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'], catagory = catagory)
        new_todo.save()

    return redirect(cid+'/')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('/todoList/'+str(cid)+'/')

def deleteCompleted(request):
    Todo.objects.filter(catagory = int(cid), complete__exact=True).delete()

    return redirect(str(cid)+'/')

def deleteAll(request):
    Todo.objects.filter(catagory = int(cid)).delete()

    return redirect(str(cid)+'/')