from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import UserFollows
from django.contrib import messages

User = get_user_model()


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
        return redirect('flux')  # Redirige l'utilisateur connecté vers le flux de posts

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flux')  # Redirige l'utilisateur vers le flux de posts après connexion
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def subscriptions_view(request):
    # Utilisateurs que l'utilisateur suit
    following = UserFollows.objects.filter(user=request.user)

    # Utilisateurs qui suivent l'utilisateur
    followers = UserFollows.objects.filter(followed_user=request.user)

    if request.method == 'POST':
        username_to_follow = request.POST.get('username')
        try:
            user_to_follow = User.objects.get(username=username_to_follow)

            # Vérifier que l'utilisateur ne suit pas déjà cette personne
            if user_to_follow == request.user:
                messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
            elif not UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
                messages.success(request, f"Vous suivez maintenant {user_to_follow.username} !")
            else:
                messages.info(request, f"Vous suivez déjà {user_to_follow.username}.")
        except User.DoesNotExist:
            # Gestion de l'erreur si l'utilisateur n'existe pas
            messages.error(request, "Cet utilisateur n'existe pas.")

    context = {
        'following': following,
        'followers': followers,
    }
    return render(request, 'subscriptions.html', context)


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")
    return redirect('subscriptions')
