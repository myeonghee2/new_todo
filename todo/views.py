from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from todo.models import Todo

# Create your views here.
@login_required(login_url='/user/login/')
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            content=request.POST["content"], 
            user=request.user,
            image=request.FILES.get("image"),
            )
        return redirect("/todo/")
    elif request.method =="GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("Invalid request method", setatus=405)