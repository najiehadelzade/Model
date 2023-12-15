from django.contrib import admin

# Register your models here.
from .models import Category, Order, OrderItem, Product, Seller

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
