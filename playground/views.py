from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Collection
from tags.models import TaggedItem
from django.db import transaction


@transaction.atomic
def say_hello(request):
    order = Order()
    order.customer_id = 1
    order.save()

    item = OrderItem()
    item.order = order
    item.product_id = 27
    item.quantity = 3
    item.price = 24.99
    return render(request, 'hello.html', {'name': 'MO'})
