from django.contrib import admin
from .models import Discount

# Discount admin
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to',
                    'discount_rate', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

admin.site.register(Discount, DiscountAdmin)
