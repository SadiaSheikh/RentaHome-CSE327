from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm,UserUpdateForm
from django.contrib.auth.models import User



# Create Signup Form
def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request,user)
            return redirect('accounts:login')
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')  

@login_required
def profile_view(request):
    u_form = UserUpdateForm(request.POST, instance = request.user)
    if u_form.is_valid():
        u_form.save()
        return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(request.POST, instance = request.user)

    return render(request, 'accounts/profile.html',{'u_form': u_form})












