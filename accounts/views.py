from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        # TODO: Test alert error output here
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # TODO: Add user login
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
