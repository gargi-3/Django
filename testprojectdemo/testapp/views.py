from django.shortcuts import render
from testapp.models import Item

# Create your views here.
def item_list(request):
    items = Item.objects.all()
    return render(request, 'testapp/item_list.html', {'items': items})