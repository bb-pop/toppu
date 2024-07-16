# accounts/urls.py
from django.urls import path
from .views import CustomLoginView, manager_dashboard, register, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('manager/', manager_dashboard, name='manager_dashboard'),
]
