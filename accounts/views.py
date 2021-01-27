from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User  # user model
from inquiry.models import Inquiry


def register(request):
    if request.method == 'POST':
        # form values
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # password check
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken.")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is taken.")
                    return redirect('register')
                else:
                    # register user
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # login
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
                    # user.save()
                    # messages.success(request, 'You have registered successfully')
                    # return redirect('login')

        else:
            messages.error(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':  # form is submitted
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = auth.authenticate(username=username, password=password)

        if user is not None:  # user exist in database
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'You are logged out')
        return redirect('index')


def dashboard(request):
    user_inquiry = Inquiry.objects.order_by('-inquiry_date').filter(user_id=request.user.id)

    context = {'inquiry': user_inquiry}
    return render(request, 'accounts/dashboard.html', context)
