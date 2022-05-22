from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegistrationForm
from lists.forms import TodoForm


def login_view(request):
    if request.method != "POST":
        return render(request, "accounts/login.html", {"form": LoginForm()})

    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, "accounts/login.html", {"form": form})
    user = authenticate(
        username=request.POST["username"], password=request.POST["password"]
    )
    if user is not None and user.is_active:
        login(request, user)
        return redirect("lists:index")
    return redirect("lists:index")


def register(request):
    if request.method != "POST":
        return render(request, "accounts/register.html", {"form": RegistrationForm()})
    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return render(request, "accounts/register.html", {"form": form})
    User.objects.create_user(
        username=request.POST["username"],
        email=request.POST["email"],
        password=request.POST["password"],
    )
    return redirect("auth:login")


def logout_view(request):
    logout(request)
    return redirect("lists:index")
