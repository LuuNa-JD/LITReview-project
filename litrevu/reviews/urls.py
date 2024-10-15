from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:ticket_id>/', views.create_review_view, name='create_review'),
    path('create_review_no_ticket/', views.create_review_no_ticket_view, name='create_review_no_ticket'),
    path('edit/<int:review_id>/', views.edit_review_view, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review_view, name='delete_review'),
]
