from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model. """
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
    )

    class Meta:
        model = models.Product
        fields = ['url', 'id', 'title', 'description', 'unit_price',
                  'inventroy', 'last_update', 'collection', 'pormotion']
