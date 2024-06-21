from django.urls import path
from .views import MyView
from . import views

urlpatterns = [
    path('myview/', MyView.as_view(), name='myview'),
    path('my_view/', views.my_view, name='my_view'),
]