from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {
        "message" : "Hello World ! ",
    }
    return render(request, 'ElProfesorFoods/home.html', context)

def menu(request):
    context = {
        "menu" : "Your menu",
    }
    return render(request, 'ElProfesorFoods/menu.html', context)

def reservation(request):
    context = {
        "reservation" : "Your reservation",
    }
    return render(request, 'ElProfesorFoods/reservation.html', context)

def my_account(request):
    context = {
        "account" : "Your account",
    }
    return render(request, 'ElProfesorFoods/your_account.html', context)

def create_account(request):
    context = {
        "account" : "Your account",
    }
    return render(request, 'ElProfesorFoods/create_account.html', context)

@login_required
def dashboard(request):
    context = {
        "dashboard" : "Your dashboard",
    }
    return render(request, 'ElProfesorFoods/dashboard.html', context)

def graphDb(request):
    context = {
        'graphics':"dashboard graphics",
    }
    return render(request, 'ElProfesorFoods/graphDb.html', context)