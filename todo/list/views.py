from django.shortcuts import render, redirect
from django.http import HttpResponse
from. models import Todo
from . forms import Todoform
def index(request):
    item=Todo.objects.all()
    form=Todoform()
    if request.method=='POST':
        form= Todoform(request.POST)
        if form.is_valid():
            form.save()
            form=Todoform()
            redirect('index')
    return render(request,'home.html',{'item':item,'form':form})
def delete (request,id):
    todo=Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=Todoform(instance=todo)
    if request.method == 'POST':
        form=Todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'update.html',{'form':form})