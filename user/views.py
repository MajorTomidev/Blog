from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
       
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome Back!, {username} ')
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render (request, 'user/userpages/register.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'This Username is taken')
                return redirect('signup')
            else:
                user =User. objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, f'Hello, {username}, your account has been created successfully')
                return redirect('home')
        else: 
            messages.error(request, "Both Passwords don't match")
            return redirect('/')
        
    else:
        return render(request, 'user/signup/signup.html')
            
def signin(request):
    if request.method== 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           messages.success(request, "You've Successfully signed in ")
           return redirect('/')
       else:
           messages.error(request, 'Your details are wrong')
           return redirect ('/')
    else:
        return render(request, 'user/login/signin.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You've logged out successfully")
    return redirect('/')
    
def home(request):
    return render(request, 'user/userpages/home.html')