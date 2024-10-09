from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirige vers la page d'accueil après inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('feed') # Redirige l'utilisateur connecté vers le flux de posts

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')  # Redirige l'utilisateur vers le flux de posts après connexion
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'users/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
