from django.shortcuts import render
from django.views.generic import ListView, DetailView
from viewapp.models import Person

# Create your views here.
class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'