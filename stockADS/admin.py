from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'size', 'in_stock']
    list_filter = ['in_stock']
    list_editable = ['size']
    search_fields = ['name']

admin.site.register(Products, ProductsAdmin)
