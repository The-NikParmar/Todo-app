from django.shortcuts import render, redirect
from .models import *
import sweetify

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
        Task.objects.create(user=user, des=request.POST['des'])
        return redirect('index')

    # Get tasks based on filter
    filter = request.GET.get('filter', 'all')
    if filter == 'pending':
        tasks = Task.objects.filter(completed=False)
    elif filter == 'completed':
        tasks = Task.objects.filter(completed=True)
    else:
        tasks = Task.objects.all()
    
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


     