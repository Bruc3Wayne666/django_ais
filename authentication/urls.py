# authentication/urls.py
from django.urls import path

from .views import register, custom_login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='achievements'), name='logout'),
    path('login/', custom_login_view, name='login'),
]
