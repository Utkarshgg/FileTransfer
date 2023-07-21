from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Employee, Identity
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'base.html')



def handlesignup(request):

    print(request.method)
    if request.method == "POST" :
        print("post hehe")
        name = request.POST['name']
        # department = request.POST['department']
        # designation = request.POST['designation']
        designation = Identity.objects.get(designation=request.POST['designation'])
        department = Identity.objects.get(department=request.POST['department'])
     #employeeid = request.POST['employee_id']
        username = request.POST['username']
        password = request.POST['pass'] 
        email = "default@gmail.com"

      #print(name, department, designation, employeeid, username, password)

        #create user
        if request.user.is_superuser:
            print("superuser hehe")
            myuser = User.objects.create_user(username = username, password = password)
           
            fruit = Employee(name=name, department=department, designation=designation, employeeid=username)
            fruit.save()
            return redirect('home')

        else:
            return HttpResponse("You are not authorized to create a user")
        


def handlelogin(request):
    if request.method=="POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user= authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            print(loginpass, loginusername)
            return HttpResponse("Invalid credentials")
   

