from django.shortcuts import render
from django.http import HttpResponse
from .models import People
from .forms import ContactForm
from .models import Contact

def home(request):
    return render(request, 'index.html')

def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = People(name=name, school=school, email=email)
        person.save()

    return HttpResponse("Success")

def people(request):
    data = People.objects.all()
    return render(request, 'people.html', {"data": data})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {"form": form})

