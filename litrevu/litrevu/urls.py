from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', user_views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('flux/', views.flux_view, name='flux'),
    path('posts/', views.user_posts, name='user_posts'),
    path('create_ticket_and_review/', views.create_ticket_and_review_view, name='create_ticket_and_review'),
    path('tickets/', include('tickets.urls')),
    path('reviews/', include('reviews.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
