from django.shortcuts import render , redirect , HttpResponse
from . models import Customer
from django.contrib.auth import authenticate, login as authlogin, logout
# Create your views here.

def dashboard(request):
    return render (request , "html/dashboard.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        
        admin = authenticate(username = uname,password=password)
        
        if admin is not None:
            authlogin(request, admin)
            # return redirect('')
            return HttpResponse('admin login')
        
        customer = Customer.objects.get(Username=uname)
        if customer:
            if customer.password == password:
                return redirect('customer')
        else:
            return redirect('signin')

    return render (request , "html/Login.html")

def registration(request):
    if request.method =='POST':
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['confirm-password']
        phone = request.POST['phone']
        membership =request.POST['membership']

        user = Customer.objects.filter(Email = email)

        if user:
            return redirect('signup')
        else:
            if password == repassword:
                newuser = Customer.objects.create(Username=uname,Email=email,password=password,phone_Number=phone,MemberShip=membership)
                if newuser:
                    return redirect('signin')
                
    return render (request , "html/registration.html")

def admindashboard(request):
    return render (request , "html/admin.html")

def customerdashboard(request):
    return render(request,'html/customer.html')

def contact(request):
    return render(request,'html/contact.html')
def about(request):
    return render(request,'html/about.html')