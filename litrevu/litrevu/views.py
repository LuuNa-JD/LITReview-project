from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'login.html')

@login_required
def flux_view(request):
    tickets = Ticket.objects.all().order_by('-time_created')
    reviews = Review.objects.all().order_by('-time_created')

    # Filtrer les critiques par utilisateur pour bloquer la création de critiques supplémentaires
    reviewed_tickets = [review.ticket.id for review in reviews if review.user == request.user]

    context = {
        'tickets': tickets,
        'reviews': reviews,
        'reviewed_tickets': reviewed_tickets,  # On passe la liste des tickets déjà critiqués
    }
    return render(request, 'flux.html', context)
