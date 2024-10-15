from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_ticket, name='add_ticket'),
    path('edit/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
]
