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
            return redirect("phonebook_django:index")
    else:
        form = newContactForm()
    return render(request, 'phonebook_django/addContact.html', {'form':form} )
