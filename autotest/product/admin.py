from django.contrib import admin
from product.models import Product
from apitest.models import Apis


# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = [
        "api_name", "api_url", "api_param", "api_method", "api_except", "api_status", "create_time", "id", "product"
    ]
    model = Apis
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_desc', 'producter', 'create_time', 'id']
    inlines = [ApisAdmin]


admin.site.register(Product, ProductAdmin)

