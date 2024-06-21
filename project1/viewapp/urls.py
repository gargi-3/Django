from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.PersonListView.as_view(), name='person_list'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('create_person/', views.create_person, name='create_person'),
]