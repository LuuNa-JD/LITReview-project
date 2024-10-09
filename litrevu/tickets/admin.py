from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')
    search_fields = ('title', 'user__username')

admin.site.register(Ticket)
