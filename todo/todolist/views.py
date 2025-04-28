from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def loginn(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        userr=authenticate(username=username,password=password)
        if userr is not None:
            auth.login(request,userr)
            return redirect('/todo')
        else:
            messages.info(request,'invalid credemtials')
            return redirect('/')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.create_user(
                  
                  email=email,
                  username=username,
                  password=password)
        user.save()
        return redirect('/loginn')
    return render(request,'register.html')
@login_required(login_url='/loginn')
def todo(request):
    if request.method=="POST":
        title=request.POST.get('title')
        obj=Todo(title=title,user=request.user)
        obj.save()
        user=request.user
        res=Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todo',{'res':res})
    res=Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res':res})
@login_required(login_url='/loginn')
def deleteedit(request,int_id):
    obj=Todo(srn=int_id,user=request.user)
    obj.delete()
    return redirect('/todo')
@login_required(login_url='/loginn')
def editor(request,int_id):
    
    if request.method=="POST":
        obj=Todo(srn=int_id,user=request.user)
        title=request.POST.get('title')
        obj.title=title
        obj.save()
        return redirect('/todo')
    else:
        obj=Todo.objects.get(srn=int_id,user=request.user)
        return render(request,'edittodo.html',{'k':obj.title})
    