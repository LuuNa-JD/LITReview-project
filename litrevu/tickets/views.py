from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

# Vue pour créer un ticket
@login_required
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')  # Redirige vers le flux des posts une fois le ticket créé
    else:
        form = TicketForm()
    return render(request, 'tickets/add_ticket.html', {'form': form})

# Vue pour modifier un ticket
@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)  # Assure que seul l'auteur peut modifier
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('flux')  # Redirige vers le flux après modification
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/edit_ticket.html', {'form': form, 'ticket': ticket})

# Vue pour supprimer un ticket
@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)  # Assure que seul l'auteur peut supprimer
    if request.method == 'POST':
        ticket.delete()
        if ticket.image:
            ticket.image.delete()
        return redirect('flux')  # Redirige vers le flux après suppression
    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})
