from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'category', 'name',
    ordering = 'category__id', 'name',
    list_filter = 'category',
