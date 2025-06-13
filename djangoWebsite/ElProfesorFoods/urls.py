from django.urls import path
from . import views

app_name = "ElProfesorFoods"

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('menu/', views.menu, name = "menu"),
    path('reservation/', views.reservation, name = "reservation"),
    path('my_account/', views.my_account, name = "my_account"),
    path('create_account/', views.create_account, name = "create_account"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('graphDb/', views.graphDb, name = "graphDb"),
]