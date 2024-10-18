from django import forms
from .models import Review
from tickets.models import Ticket

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ReviewNoTicketForm(forms.ModelForm):
    # Formulaire pour le ticket
    ticket_title = forms.CharField(max_length=128, label="Titre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ticket_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Description")
    ticket_image = forms.ImageField(required=False, label="Télécharger fichier", widget=forms.FileInput(attrs={'class': 'form-control'}))

    # Formulaire pour la critique
    review_comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Commentaire")

    class Meta:
        model = Review
        fields = ['review_comment']
