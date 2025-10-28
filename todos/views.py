
from .models import Todo
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

# also get request
@login_required(login_url="login_user")
def home_page(request):
    if request.user.is_staff or request.user.is_superuser:
        todos_count = Todo.objects.count()
    else:
        # інакше тільки його власні
        todos_count = Todo.objects.filter(user=request.user).count()
    # return render(request,"todos/index.html", {"todos": todos})
    return render(request, "todos/index.html", {"todos_count":todos_count})



# view todos get request
def show_todos(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            todos =  Todo.objects.all()
        else:
            todos = Todo.objects.filter(user = request.user)
    else:
        return redirect("login_user")
        
    done_todo = todos.filter(is_done = True)
    not_done_todo = todos.filter(is_done = False)
    return render(request, "todos/todo.html", {"todos":todos})


# create post request
@login_required(login_url='login_user')
def create_todo(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST.get("title")
            description = request.POST.get("description")
            Todo.objects.create(user = request.user,title=title, description=description )
            # Todo.objects.create(user_name=user_name,title=title, description=description)
            return redirect("show_todos")
        else:
            return redirect("login_user")
    return render(request, "todos/create_todo.html")

# delete request

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect("show_todos")


# update todo - put request
def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":

        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")

        todo.save()
        return redirect("show_todos")
    return render(request, "todos/update_todo.html", {"todo": todo})
    

def toggle_todo(request, pk):
    if request.user.is_superuser:
        
        todo = get_object_or_404(Todo, pk=pk)
    else:
        todo = get_object_or_404(Todo, pk=pk, user = request.user)

    todo.is_done = not todo.is_done
    todo.save()
    return redirect("show_todos")