from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterForm, ProfileForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully created an account')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def Login(request):
    return render(request, 'Users/login.html')

def Profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully!!')
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'Users/profile.html', {'form': form})