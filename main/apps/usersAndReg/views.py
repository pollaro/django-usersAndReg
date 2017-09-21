from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Users
import bcrypt

def index(request):
    return render(request,'usersAndReg/index.html')

def register(request):
    print 'Register'
    errors = Users.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            print tag
            messages.error(request,error,extra_tags=tag)
        return redirect('index')
    elif len(Users.objects.filter(email=request.POST['email'])) != 0:
        messages.error(request,'Email is already in use',extra_tags='emailInUse')
        return redirect('index')
    else:
        hashedPW = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        Users.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['email'],password=hashedPW)
        u1 = Users.objects.get(email=request.POST['email'])
        return redirect(reverse('success',args=[u1.id]))

def login(request):
    user = Users.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]
        encodepw=request.POST['password'].encode()
        if bcrypt.checkpw(encodepw,user.password.encode()):
            return redirect(reverse('success',args=[user.id]))
    else:
        messages.error(request,'Email and Password not recognized',extra_tags='login')
        return redirect('index')

def success(request,id):
    context = {
        'user':Users.objects.get(id=id)
    }
    return render(request,'usersAndReg/success.html',context)
