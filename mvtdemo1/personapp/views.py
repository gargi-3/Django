from django.shortcuts import render
from .models import Person

# Create your views here.
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'personapp/person_list.html', {'persons': persons})