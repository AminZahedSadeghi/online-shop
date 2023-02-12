from django.contrib import admin

from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['datetime_created']
