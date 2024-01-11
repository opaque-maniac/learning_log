from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm

# View for the register page
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, authenticate(user))
            return redirect(reverse('learning_log:home'))
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {
        'form': form
    })

# View for the login page
def login_view(request):
    return LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm)(request)

# View for the logout function
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('learning_log:landing'))
