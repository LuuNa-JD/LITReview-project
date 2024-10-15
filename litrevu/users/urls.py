from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Page de connexion
    path('signup/', views.signup_view, name='signup'),  # Page d'inscription
    path('logout/', views.logout_view, name='logout'),  # Page de déconnexion
    path('subscriptions/', views.subscriptions_view, name='subscriptions'),  # Page des abonnements
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),  # Page de désabonnement
]
