from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = TodoForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			print('Invalid form')
	else:
		todos = Todo.objects.all()
		return render(request,'todo.html',{'todos':todos})

def delete(request, todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.delete()
	return redirect('index')