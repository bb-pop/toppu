# accounts/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from .forms import UserUpdateForm


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

@login_required
@user_passes_test(is_manager)
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'user_detail.html', {'form': form, 'user': user})