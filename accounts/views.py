from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Get Form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['password2']

        # Check if passwords match
        if password == cnf_password:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered")
                return redirect('register')
            else:
                # Looks Good
                user = User.objects.create_user(username=username, email=email, first_name=first_name,
                                                last_name=last_name, password=password)
                # # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(request, 'registered Successfully')
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In..')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out successfully')
        return redirect('index')
    else:
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
