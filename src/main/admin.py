from django.contrib import admin

from main.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

admin.site.register(Product, ProductAdmin)
