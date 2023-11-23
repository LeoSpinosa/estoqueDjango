from django.contrib import admin
from .models import Products, Categories

class ProductsAdmin(admin.ModelAdmin):

    list_display = ['id','name', 'price', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['name']

admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)

