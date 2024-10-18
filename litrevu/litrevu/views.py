from django.shortcuts import render
from itertools import chain
from tickets.models import Ticket
from reviews.models import Review
from tickets.forms import TicketForm
from reviews.forms import ReviewForm
from django.shortcuts import redirect
from users.models import UserFollows
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'login.html')

@login_required
def flux_view(request):
    # Récupérer les utilisateurs que l'utilisateur suit
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)

    # Inclure aussi les propres billets et critiques de l'utilisateur
    followed_users = list(followed_users) + [request.user.id]

    # Récupérer les billets et critiques des utilisateurs suivis
    tickets = Ticket.objects.filter(user__in=followed_users).order_by('-time_created')
    reviews = Review.objects.filter(ticket__in=tickets).order_by('-time_created')

    # Récupérer les billets que l'utilisateur connecté a déjà critiqués
    reviewed_tickets = Review.objects.filter(user=request.user).values_list('ticket_id', flat=True)

    # Ajouter un attribut "post_type" pour identifier les billets et critiques
    for ticket in tickets:
        ticket.post_type = 'ticket'
        ticket.is_owner = (ticket.user == request.user)
        # Récupérer toutes les critiques associées à chaque billet
        ticket.reviews = reviews.filter(ticket=ticket)

    context = {
        'posts': sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True),
        'reviewed_tickets': reviewed_tickets,  # Utilisé dans le template pour savoir si l'utilisateur a déjà critiqué un billet
    }
    return render(request, 'flux.html', context)

@login_required
def user_posts(request):
    # Récupérer tous les tickets créés par l'utilisateur connecté
    user_tickets = Ticket.objects.filter(user=request.user)

    # Récupérer toutes les critiques créées par l'utilisateur
    user_reviews = Review.objects.filter(user=request.user)

    # Récupérer toutes les critiques faites sur les tickets de l'utilisateur par d'autres utilisateurs
    reviews_on_user_tickets = Review.objects.filter(ticket__user=request.user).exclude(user=request.user)

    context = {
        'user_tickets': user_tickets,
        'user_reviews': user_reviews,
        'reviews_on_user_tickets': reviews_on_user_tickets,
    }

    return render(request, 'posts.html', context)


@login_required
def create_ticket_and_review_view(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            # Créer le billet (Ticket)
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            # Créer la critique (Review) associée au billet
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket

            # Récupérer la note du POST
            rating = request.POST.get('review_rating')
            if not rating:
                return render(request, 'tickets/create_ticket_and_review.html', {
                    'ticket_form': ticket_form,
                    'review_form': review_form,
                    'error_message': 'Vous devez sélectionner une note.'
                })
            review.rating = int(rating)  # Convertir la note en entier
            review.save()

            return redirect('flux')  # Redirige après la création
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(request, 'create_ticket_and_review.html', {
        'ticket_form': ticket_form,
        'review_form': review_form
    })
