from django.contrib import admin

from gumroadclone.products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
