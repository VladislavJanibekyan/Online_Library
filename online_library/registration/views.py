from django.shortcuts import render, redirect
from .forms import UserCreate
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    form = UserCreate()
    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('profile')
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    return render(request, 'registration/login.html')
@login_required
def profile(request):
    return render(request, 'registration/profile.html')