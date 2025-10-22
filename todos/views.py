from django.http import HttpResponse
from .models import Todo
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# also get request
def home_page(request):
    todos_count = Todo.objects.count()
    # return render(request,"todos/index.html", {"todos": todos})
    return render(request, "todos/index.html", {"todos_count":todos_count})



# view todos get request
def show_todos(request):
    todos =  Todo.objects.all()
    
    return render(request, "todos/todo.html", {"todos":todos})


# create post request
def create_todo(request):
    if request.method == "POST":

        title = request.POST.get("title")
        user_name = request.POST.get("user_name")
        description = request.POST.get("description")
        Todo.objects.create(user_name=user_name,title=title, description=description)
        return redirect("show_todos")
    return render(request, "todos/create_todo.html")

# delete request

def delete_todo(request, id):
    todos = Todo.objects.get(id=id)
    todos.delete()
    return redirect("show_todos")


# update todo - put request
def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":

        todo.user_name = request.POST.get("user_name")
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")

        todo.save()
        return redirect("show_todos")
    return render(request, "todos/update_todo.html", {"todo": todo})
    