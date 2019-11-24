from django.shortcuts import render,redirect
from firstapp.forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from firstapp.models import SignUP
from django.contrib.auth import authenticate

# Create your views here.
from django.contrib import redirects
def index(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            name=request.POST["Name"]
            email=request.POST["Email"]
            password=request.POST["Password"]
            mobile=request.POST["Mobile"]
            address=request.POST["Address"]
            f = User.objects.create_user(username=name,email=email,password=password)
            SignUP.user=name
            SignUP.Mobile=mobile
            SignUP.Address=address
            f.save()
            data=User.objects.all()
            # return HttpResponse(User.username)
            f = SignUP(Mobile=mobile, Address=address)
            f.save()
            return redirect('/login/')
    else:
        form = signupform()
        print("not")
    return render(request, "register.html",{"form":form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse("success")
        else:
                return HttpResponse("Your account was inactive.")
    else:
        return render(request,'login.html')