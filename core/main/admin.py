from django.contrib import admin
from .models import Product, Category, Color, Brand, Slider
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'productName', 'price']
    list_display_links = ['productName']
    search_fields = ['productName', 'price']

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Slider)