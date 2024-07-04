from django.shortcuts import render, get_object_or_404
from . models import Pet, Product

# Create your views here.
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'petstore413/pet_list.html', {'pets':pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'petstore413/pet_detail.html', {'pet':pet})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'petstore413/product_list.html', {'products':products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'petstore413/product_detail.html', {'product':product})
