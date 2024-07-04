from django.contrib import admin
from . models import Cart, CartItem, Pet, Product

# Register your models here.
admin.site.register(Pet)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)