from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,"home.html")

def SignupPage(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        sex = request.POST.get('sex') 
        
        # Create the user with the required fields
        my_user = User.objects.create_user(username=email, email=email, password=pass1)
        
        # Set additional fields
        my_user.first_name = fname
        my_user.last_name = lname
        # If you need 'sex', consider adding it to a custom user model
        # my_user.sex = sex

        my_user.save()
        return redirect('login')
    
    return render(request, "signup_page.html")


def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        user=authenticate(request,username=email, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            return HttpResponse('username and password is incorrect')
       
    
    return render(request,"login_page.html")


def user_logout(request):
    logout(request)
    return redirect("login")
    
