from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'quantity', 'image']
    list_filter = ['quantity']
    search_fields = ['name']
    ordering = ['product_id']
