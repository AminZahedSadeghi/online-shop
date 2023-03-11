from django.contrib import admin

from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentIndline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ['user', 'body', 'is_reply']


@admin.register(Product)
class AdminProduct(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['datetime_created']

    inlines = [
        CommentIndline,
    ]


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'body', 'is_reply']
