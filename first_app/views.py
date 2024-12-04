from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, "profile.html")

def signinPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            print(form.cleaned_data)
            return redirect('login')
    else:
        form = RegistrationForms()
    return render(request, "signup.html", {"form": form})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password = userpass)
                if user is not None:
                    messages.success(request, "Logged in successfully")
                    login(request, user)
                    return redirect('profile')
            else:
                messages.warning(request, "Invalid username or password")
        else:
            form = AuthenticationForm()
        return render(request, "login.html", {"form" : form})

@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login')

def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password changed successfully")
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': form, 'type': 'Change Password'})

@login_required
def reset_password(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset successfully")
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'password.html', {'form': form, 'type': 'Reset Password'})

@login_required
def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = changeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('profile')
        else:
            form = changeUserData(instance=request.user)
        return render(request, 'password.html', {'form': form , 'type': 'Update Profile'})