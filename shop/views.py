from django.shortcuts import render,redirect
from . models import Product,Category,Profile
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . forms import SignupForm,UpdateUserForm,UpdatePassswordForm,UpdateUserInfo
from django.contrib.auth.models import User
from django.db.models import Q
import json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress

def hello(request):
    all_products = Product.objects.all()
    return render(request,'shop/index.html',{'products':all_products})

def about(request):
    return render(request,'shop/about.html')

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id)
        form = UpdateUserInfo(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None,instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request,(" اطلاعات کاربری شما ویرایش شد"))
            return redirect('home')
        return render(request,'shop/update_info.html',{'form':form,'shipping_form':shipping_form})
    else:
        messages.success(request,(" ابتدا باید وارد حساب کاربری خود شوید"))
        return redirect('home')


def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request,("مشکلی در ورود وجود دارد"))
            return redirect("login")
    else:
        return render(request,'shop/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")

def signup_user(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password1)
            login(request,user)
            messages.success(request,("حساب کاربری شما ساخته شد"))
            return redirect("update_info")  
        else: 
            messages.success(request,("مشکلی به وجود آمده است"))
            return redirect("signup")
        
    else:
  
        return render(request,'shop/signup.html',{'form':form})
    

def update_user(request):
   
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,(" حساب کاربری شما ویرایش شد "))
            return redirect('home')
        return render(request,'shop/update_user.html',{'user_form':user_form})
    else:
        messages.success(request,(" ابتدا باید وارد حساب کاربری خود شوید"))
        return redirect('home')
    

def update_password(request):
    if request.user.is_authenticated:
        current_user= request.user
        if request.method=='POST':
            form=UpdatePassswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,(" رمز با موفقیت ویرایش شد"))
                login(request,current_user)
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                return redirect('update_password')
        else:
            form=UpdatePassswordForm(current_user)
            return render(request,'shop/update_password.html',{'form':form})
    else:
         messages.success(request,(" ابتدا باید وارد حساب کاربری خود شوید"))
         redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'shop/product.html',{'product':product})

def category(request,cat):
    cat = cat.replace("-"," ")
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request,'shop/category.html',{'category':category,'products':products,})
    except:
        messages.success(request,(" این دسته بندی وجود ندارد! "))
        return redirect("home")
    


def search(request):
    if request.method=='POST':
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched)|Q(description__icontains=searched))
        if not searched:
            messages.success(request,(" این محصول وجود ندارد! "))
            return render(request,'shop/search.html',{})
        else:
            return render(request,'shop/search.html',{'searched':searched})

