from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        if name is not None or age is not None:
            p = Person(name=name, age=age)
            p.save()
            messages.info(request, "User Added")
        else:
            messages.info(request, "Invalid credentials")
    return render(request,'home.html')