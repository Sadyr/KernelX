from django.contrib import admin

# Register your models here.
from .models import Items, Category, Tag

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('tags',)
