from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import random
from .forms import TodoForm
from .models import Todo


# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(quest=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.isComplete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(isComplete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
def rndQuest(request):
    yapilacaklar = ["Odevleri yap","yine odevleri yap","odevler daha bitmedi","Finaller","ders çalış"]
    sayi = random.randint(0, 4)
    new_todo = Todo(quest=yapilacaklar[sayi])
    new_todo.save()

    return redirect('index')