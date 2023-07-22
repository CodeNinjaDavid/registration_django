from django.shortcuts import render
from django.http import HttpResponse
from .models import People
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def get_next_id():
    # Custom function to get the next available primary key value
    last_record = People.objects.last()
    if last_record is not None:
        return last_record.id + 1
    return 1  # If there are no records, start with ID 1

def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        # Get the next available primary key value
        next_id = get_next_id()

        # Manually assign the primary key and save the record
        person = People(id=next_id, name=name, school=school, email=email)
        person.save()

        return HttpResponse("Success")

    return HttpResponse("No data received")

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

def delete(request, id):
    dd = People.objects.get(id=id)
    dd.delete()

    return HttpResponse("Delete successful")

def update(request, id):
    l = People.objects.get(id=id)

    return render(request, "edit.html", {"l": l})
