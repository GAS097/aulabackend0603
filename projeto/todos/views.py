from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo_list_old(request):
    nome = 'Gabriel'
    alunos = ['1.Thiago', '2.Kayo', '3.Rodrigo']
    return render(request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos})

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})