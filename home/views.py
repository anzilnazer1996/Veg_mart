from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Vegetables,Userinfo


# Create your views here.

def home(request):
    data=Vegetables.objects.all()
    details={'details':data}
    if request.method=='POST':
        product_id=request.POST.get('item_id')
        
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product_id)
            if quantity:
                cart[product_id]=quantity+1
            else:
                cart[product_id]=1    
        else:
            cart={}
            cart[product_id]=1
        request.session['cart']=cart 
        return redirect('home') 
    return render(request,'home.html',details)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        profile_pic=request.POST.get('profile_pic')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.success(request,'successfully created')
                return redirect('login')
        else:
            messages.info(request,'Passwords does not match')
            return redirect('register')
    else:    
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session.get('cart').clear()
            return redirect('home')
        else:
            messages.info(request,'invalid username and password') 
            return redirect('login') 
    else:          
        return render(request,'login.html')
def cart(request):
    ids=list(request.session.get('cart').keys())
    data=Vegetables.objects.filter(id__in=ids)
    detail={'details':data}
    if request.method=='POST':
        product_id=request.POST.get('item_id')        
    return render(request,'cart.html',detail)
                
    


