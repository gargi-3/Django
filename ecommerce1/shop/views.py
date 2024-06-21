from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})