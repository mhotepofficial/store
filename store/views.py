#!/usr/bin/env python3
""" Views for the store app. """
from rest_framework import viewsets
from . import models
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):
    """ Viewset for products. """
    queryset = models.Product.objects.select_related(
        'collection'
    ).prefetch_related('pormotion').all()
    serializer_class = serializers.ProductSerializer
