from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import CustomUserCreationForm, CustomErrorList, UsernamePasswordResetForm

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})


def username_password_reset_request(request):
    if request.method == "POST":
        form = UsernamePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Get username
            try:
                user = User.objects.get(username=username)  # Fetch user
                return redirect(reverse("password_reset_confirm", args=[user.pk]))  # Redirect to reset page
            except User.DoesNotExist:
                form.add_error("username", "This username does not exist.")  # Show error if username is invalid

    else:
        form = UsernamePasswordResetForm()

    return render(request, "accounts/password_reset.html", {"form": form})


def username_password_reset_confirm(request, user_id):
    User = get_user_model()

    try:
        user = User.objects.get(pk=user_id)  # Ensure user exists
    except User.DoesNotExist:
        return redirect("password_reset")  # Redirect back if user ID is invalid

    if request.method == "POST":
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        if new_password == confirm_password:
            user.password = make_password(new_password)  # Hash and save new password
            user.save()
            return redirect("accounts.login")  # Redirect back to login page
        else:
            return render(request, "accounts/password_reset_confirm.html", {"error": "Passwords do not match."})

    return render(request, "accounts/password_reset_confirm.html", {"user": user})