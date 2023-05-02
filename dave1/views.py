from django.shortcuts import render,redirect 
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate, logout 
from datetime import datetime
from dave1.models import Contact
from django.contrib import messages  

# Create your views here.

def index(request):
    context ={
        'python':"django",
        'variable':'this is sent'
    }
    # messages.success(request,"this is test message")
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html",context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email= email,phone= phone,desc= desc,date= datetime.today())
        contact.save()
        messages.success(request,"YOUR message has been sent !!!")
    return render(request,'contact.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials 
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login") 

