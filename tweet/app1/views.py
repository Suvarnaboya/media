from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.models import *

# Create your views here.
def feed(request):
    res=tweeter.objects.all()[::-1]
    return render(request,'feed.html',{'data':res})

def loginView(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        u=request.POST.get('usern')
        p=request.POST.get('passw')
        result = authenticate(request,username=u,password=p)

        if result is not None:
            login(request,result)   
            return redirect('profile') 
        else:
            return render(request,'login.html')                      
    return render(request,'login.html')


def userExists(x):
    if User.objects.filter(username=x).exists():
        return True
    else:
        return False
    
def length(z):
    if len(z)>8:return True
    else:return False

def spaceExists(y):
    if len(y.split())>1:
        return True
    else:
        return False
    
def checkPass(a):
    if len(a)>8:return True
    else:return False

def isSpl(b):
    if b.isalnum():
        return False
    else:return True

def register(request):
    if request.method=="POST":
        u=request.POST.get('usern')    
        f=request.POST.get('fname')    
        l=request.POST.get('lname')    
        m=request.POST.get('mail')    
        p=request.POST.get('passw')
        print(u,f,l,m,p)

        if userExists(u):
            d={'warn':"Arey Thamudu alreadt username taken !"}
            return render(request,'register.html',d)
        if not length(u):
            d={'warn':"Username should graterthan 8"}
            return render(request,'register.html',d)
        
        if spaceExists(u):
            d={'warn':"Username should not contain spaces"}
            return render(request,'register.html',d)
        
        if not checkPass(p):
            d={'warn':"Password should atleast 8 characters"}
            return render(request,'register.html',d)
        
        if not isSpl(p):
            d={'warn':"You havnt used special character"}
            return render(request,'register.html',d)
        
        obj=User.objects.create_user(
            username=u,
            first_name=f,
            last_name=l,
            email=m,
            password=p
            )
        obj.save()

    return render(request,'register.html')

@login_required(login_url='login')
def postView(request):
    if request.method=="POST":
        t=request.FILES.get('title')
        c=request.POST.get('cap')
        u=request.user.username
        obj=tweeter(person=u,image=t,caption=c)
        obj.save()
    return render(request,'post.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

def logoutView(request):
    logout(request)
    return redirect('login')


def single(request,rid):
    res=tweeter.objects.get(id=rid)
    return render(request,'single.html',{'data':res})


def updateView(request,rid):
    obj=tweeter.objects.get(id=rid)
    if request.method=="POST":
        t=request.FILES.get('title')
        c=request.POST.get('caption')
        o=tweeter.objects.get(id=rid)
        o.image=t
        o.caption=c
        o.save()
        return redirect('home')
    return render(request,'update.html',{'data':obj})

def deleteView(request,rid):
    obj=tweeter.objects.get(id=rid)
    obj.delete()
    return redirect('home')

@login_required(login_url="login")
def manu(request):
    if request.method=="POST":
        b=request.POST.get('brand')
        c=request.POST.get('ceo')
        t=request.POST.get('turnover')
        obj=Manufacturer(brand=b,ceo=c,turnover=t)
        obj.save()
    return render(request,'manu.html')


@login_required(login_url="login")
def createCar(request):
    if request.method=="POST":
        n=request.POST.get('car_name')
        y=request.POST.get('year')
        mid=request.POST.get('mid')
        if Manufacturer.objects.filter(id=mid).exists():
            m=Manufacturer.objects.get(id=mid)
            f=request.POST.get('fuel')

            obj=Car(name=n,year=y,manufacture=m,fuel=f)
            obj.save()
        else:
            d={'warn':"Wrong Manufacturer ID"}
            return render(request,'create.html',d)

    return render(request,'create.html')




def showCars(request):
    objs=Car.objects.all()[::-1]
    if request.method=="POST":
        b=request.POST.get('brand')
        objs=Car.objects.filter(manufacture__brand__icontains=b)
    return render(request,'car.html',{'data':objs})