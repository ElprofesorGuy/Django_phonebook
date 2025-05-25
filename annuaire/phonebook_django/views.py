from django.shortcuts import render,redirect
from .models import Contact
from .forms import newContactForm

# Create your views here.
def phonebook(request):
    context = {"contacts" : Contact.objects.all()}
    return render(request, "phonebook_django/phonebook.html", context)


def addContact(request):
    if request.method == "POST":
        form = newContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("phonebook_django:phonebook")
    else:
        form = newContactForm()
    return render(request, 'phonebook_django/addContact.html', {'form':form} )

def remove(request, contact_id):
    contact_delete = Contact.objects.get(pk = contact_id)
    contact_delete.delete() 
    return redirect("phonebook_django:phonebook")

def edit(request, contact_id):
    contact_edit = Contact.objects.get(pk=contact_id)
    if request.method == "POST":
        form = newContactForm(request.POST, instance = contact_edit)
        if form.is_valid():
            form.save()
            return redirect("phonebook_django:phonebook")
    else:
        form = newContactForm(instance = contact_edit)
    return render(request, 'phonebook_django/editContact.html', {'form':form} )