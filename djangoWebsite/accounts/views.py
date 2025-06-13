from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def login_user(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('ElProfesorFoods:dashboard')
        else:
            messages.info(request, "Identifiant ou mot de pass incorrect")
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect("accounts:login_user");
 
def register_user(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ElProfesorFoods:dashboard")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form" : form})
