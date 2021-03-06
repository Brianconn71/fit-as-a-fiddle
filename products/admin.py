from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    '''adds a product and category to backend admin'''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    read_only = ('rating',)

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
