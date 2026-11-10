from django.contrib import admin
from .models import Category, Flower


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'flowers_count', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description="Liczba kwiatów")
    def flowers_count(self, obj):
        return obj.flowers.count()


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'latin_name', 'category', 'height_cm', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'latin_name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'is_available')

    fieldsets = (
        ("Podstawowe informacje", {
            'fields': ('name', 'latin_name', 'slug', 'category', 'added_by', 'description')
        }),
        ("Szczegóły", {
            'fields': ('height_cm', 'price', 'is_available')
        }),
    )