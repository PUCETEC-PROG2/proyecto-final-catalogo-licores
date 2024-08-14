from django.contrib import admin
from .models import Category, Product, Client, Purchase_order, Order_item

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Purchase_order)
admin.site.register(Order_item)
