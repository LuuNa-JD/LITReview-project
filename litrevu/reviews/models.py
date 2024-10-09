from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from tickets.models import Ticket


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=128)
    comment = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Critique de {self.user.username} sur {self.ticket.title}"
