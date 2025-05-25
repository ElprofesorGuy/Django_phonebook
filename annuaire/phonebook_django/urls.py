from django.urls import path
from . import views

app_name = "phonebook_django"

urlpatterns = [
    path('', views.phonebook, name = "phonebook"),
    path('newContact/', views.addContact, name = 'addContact'),
    path('remove/<int:contact_id>/', views.remove, name = "remove"),
    path('edit/<int:contact_id>/', views.edit, name = "edit"),
]