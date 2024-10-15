from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .forms import ReviewNoTicketForm
from tickets.models import Ticket
from .models import Review

@login_required
def create_review_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form, 'ticket': ticket})

@login_required
def create_review_no_ticket_view(request):
    if request.method == 'POST':
        form = ReviewNoTicketForm(request.POST, request.FILES)
        if form.is_valid():
            # Créer un ticket avec les données du formulaire
            ticket = Ticket.objects.create(
                title=form.cleaned_data['ticket_title'],
                description=form.cleaned_data['ticket_description'],
                image=form.cleaned_data['ticket_image'],
                user=request.user
            )

            # Créer la critique associée
            Review.objects.create(
                ticket=ticket,
                rating=form.cleaned_data['review_rating'],
                comment=form.cleaned_data['review_comment'],
                user=request.user
            )

            return redirect('flux')  # Rediriger vers la page du flux après création
    else:
        form = ReviewNoTicketForm()

    return render(request, 'reviews/create_review_no_ticket.html', {'form': form})

@login_required
def edit_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('flux')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('flux')
    return render(request, 'reviews/delete_review.html', {'review': review})
