# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

def is_manager(user):
    return user.role == 'manager'

@login_required
@user_passes_test(is_manager)
def manager_dashboard(request):
    managers = CustomUser.objects.filter(role='manager')
    cashiers = CustomUser.objects.filter(role='cashier')
    users = list(managers) + list(cashiers)
    return render(request, 'manager_dashboard.html', {'users': users})

