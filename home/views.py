from django.shortcuts import render,redirect,HttpResponse
from home.models import lis,contact_details,sign
from django.contrib import messages
from django.contrib.auth import authenticate,login
from datetime import datetime


def index(request):
    return render(request,'index.html')

def sign_up(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        opass=request.POST.get('opass')
        cpass=request.POST.get('cpass')

        if opass == cpass:
            si=sign(name=name,password=opass,email=email)
            si.save()
            messages.success(request,"You Successfully signed in !!")
            return redirect('/')
        else:
            messages.error(request,'Password Not matching')
            return redirect('/sign')
    else:
        return render(request,'sign_up.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        date=datetime.today()
        con=contact_details(name=name,phone=phone,desc=desc,date=date)
        con.save()
        messages.success(request,"You Successfully signed in !!")
        return redirect('/contact')
    
    return render(request,'contact.html')

def sign_in(request):
    if request.method == "POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Successfully signed in !!")
            return redirect('/list/'+uname)
        else:
            return redirect('/')
    else:    
        return render(request,'sign_in.html')


def list(request,user):
    if request.method =="POST":
        title=request.POST.get('title')
        date=datetime.now()
        l=lis(name=title,uname=request.user,date=date)
        l.save()
        context={
            'name':l.name,
            'dat':l.date,
            'uname':l.uname,
        }
        return redirect('/list/'+str(l.uname))

    # data=lis.objects.all()
    data=lis.objects.all()

    context={
        'names':data,
        'user':user
    }
    return render(request,'list.html',context=context)

def delete(request,event_id):
    event=lis.objects.get(id=event_id)
    x=str(event.uname)
    event.delete()
    return redirect('/list/'+x)


def err(request):
    return HttpResponse('Sign in first !!')