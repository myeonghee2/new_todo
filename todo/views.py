from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from todo.models import Todo

# Create your views here.
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            "todos":todos,
        }
        return render(request, 'todo/index.html', context)
    else:
        return HttpResponse("Invalid request method", setatus=405)


@login_required(login_url='/user/login/')
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            content=request.POST["content"])
        return redirect("/todo/")
    elif request.method =="GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("Invalid request method", setatus=405)
    
def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        "todo":todo,
    }
    return render(request, 'todo/detail.html', context)

