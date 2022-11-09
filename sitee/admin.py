from django.contrib import admin

# Register your models here.
from sitee.models import *


class ProductInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
