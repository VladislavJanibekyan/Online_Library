from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreate, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserProfile



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
    id_=request.user.id
    userprof = get_object_or_404(UserProfile, user=id_)
    return render(request, 'registration/profile.html', {'prof': userprof})

@login_required
def profile_update(request):
    userprof = Profile(instance=request.user.userprofile)
    if request.method == "POST":
        userprof = Profile(request.POST, request.FILES, instance=request.user.userprofile)
        if userprof.is_valid():
            userprof.save()
            return redirect('profile')
    return render(request, 'registration/profile_update.html', {'form': userprof})