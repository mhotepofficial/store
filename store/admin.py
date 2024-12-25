from django.contrib import admin
from . import models
from django.db.models import Count
from django.urls import reverse
from urllib.parse import urlencode
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', 'ProductFilterAdmin']


    class ProductFilterAdmin(admin.SimpleListFilter):
        title = 'inventory'
        parameter_name = 'inventory'
        def lookups(self, request, model_admin, field):
            return [
                ('<10', 'low')
            ]
            def queryset(self, request, queryset):
                if self.value() == '<10':
                    return queryset.filter(inventory__lt=10)
                return queryset

    @admin.display(ordering='inventroy')
    def inventory_status(self, product):
        if product.inventroy < 10:
            return 'Low'
        return 'OK'

    def collection_title(self, product):
        return product.collection.title


class CustomrAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'customer_orders']
    list_editable = ['membership']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='customer_orders')
    def customer_orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({'customer__id': str(customer.id)})
        )
        return format_html('<a href="{}">{}</a>', url, customer.customer_orders)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            customer_orders=Count('order')
        )


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({'collection__id': str(collection.id)})
        )
        return format_html('<a href="{}">{}</a>', url,
                           collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Customer, CustomrAdmin)
admin.site.register(models.Product, ProductAdmin)
