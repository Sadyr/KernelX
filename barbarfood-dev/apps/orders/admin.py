from django.contrib import admin
from apps.orders.models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(Delivery)


class CartProductInline(admin.StackedInline):
    extra = 0
    model = CartItems

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartProductInline]