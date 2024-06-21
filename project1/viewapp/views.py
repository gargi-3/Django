from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from viewapp.models import Person
from .forms import PersonForm

# Create your views here.
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'viewapp/create_person.html', {'form': form})

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(first_name__icontains=query)
        return queryset

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'