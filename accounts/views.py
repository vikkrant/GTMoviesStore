from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import CustomUserCreationForm, CustomErrorList, UsernamePasswordResetForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import CustomPasswordResetForm

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
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect("password_reset")

    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST, user=user)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]

            if check_password(new_password, user.password):
                form.add_error("new_password", "New password cannot be the same as the old password.")
            else:
                try:
                    validate_password(new_password, user)
                    user.password = make_password(new_password)
                    user.save()
                    return redirect("accounts.login")
                except ValidationError as e:
                    form.add_error("new_password", e.messages)

    else:
        form = CustomPasswordResetForm(user=user)

    return render(request, "accounts/password_reset_confirm.html", {"form": form})