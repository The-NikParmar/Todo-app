from django.shortcuts import render, redirect,get_object_or_404
from .models import *
import sweetify
from django.http import JsonResponse
from django.utils.timezone import now

# Create your views here.

def signup(request):        
        if request.POST:
            try:
                 User.objects.get(email=request.POST['email'])
                 sweetify.info(request,"Email is alredy Exists...")
                 return redirect('signup')
            except:
                 
                if request.POST['pass1']==request.POST['pass2']:
                    print("hello")
                    user = User.objects.create(
                        name = request.POST['name'],
                        email = request.POST['email'],
                        password = request.POST['pass2'], 
                    )
                    sweetify.success(request,"Signup Successfully.....")
                    return redirect('login')
                else:
                    sweetify.info(request,"Password and Conifrm Password dose not match...")
                    return redirect('signup')
        else:
            print("why")
            return render(request,"signup.html")

def login(request):
    if request.POST:
         user =  User.objects.get(email=request.POST['email'])
         if user.password == request.POST['password']:
              request.session['email'] = user.email
              sweetify.success(request,"Login Successfully...")
              return redirect('index')
         else:
              sweetify.error("password  is wrong!!!!")
              return redirect('login')
    else:
         print("else part of logins")
         return render(request,"login.html")

def index(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Task.objects.create(user=user, des=request.POST['des'],created_at=now())
        return redirect('index')


    filter = request.GET.get('filter')
    if filter == 'pending':
        tasks = Task.objects.filter(user=user,completed=False)
    elif filter == 'completed':
        tasks = Task.objects.filter(user=user,completed=True)
    else:
        tasks = Task.objects.filter(user=user)
    
    context = {
        'task': tasks,
        'filter': filter,
    }
    return render(request, 'index.html', context)
    
def logout(request):
     del request.session['email']
     return redirect('login')

def pending(request):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        pending_tasks = Task.objects.filter(user=user, completed=False)
        return render(request, 'index.html', {'pending_tasks': pending_tasks})
    else:
        return redirect('login')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete_all_task(request):
    user = User.objects.get(email=request.session['email'])
    task = Task.objects.filter(user=user)
    if task:
        task.delete()
        sweetify.success(request,"All Tasks Delete Successfully...")
        return redirect('index')
    else:
        sweetify.info(request,"No Task Found....")
        return redirect('index')
    
def edit_task(request,id):
    task=Task.objects.get(id=id)
    print(task)
    if request.POST:
        task.des=request.POST['taskDescription']
        task.save()
        return redirect('index')   
    
def delete_task(request,id):
    task=Task.objects.get(id=id)
    print(task)
    task.delete()
    return redirect('index') 

        
    

    

     