from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name","price","stock")

class ShippingAddressAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("order","customer","address")

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
