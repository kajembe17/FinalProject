from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    """ Render register template"""
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # Check if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('register')
                else:
                    # Otherwise, everything is good
                    # create new user
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, 
                    username=username, email=email, password=password)
                    # save user details display success message and redirect to login
                    user.save()
                    messages.success(request, 'You have registered successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """ Render login template"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # if user is found
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username and/or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """ Logout View """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are logged out")
        return redirect('index')


def dashboard(request):
    """ Render dashboard template"""
    return render(request, 'accounts/dashboard.html')
