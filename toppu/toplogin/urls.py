# accounts/urls.py
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('manager/', manager_dashboard, name='manager_dashboard'),
    path('user/<int:user_id>/', user_detail, name='user_detail'),
]
