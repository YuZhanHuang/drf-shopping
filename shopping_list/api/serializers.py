from rest_framework import serializers

from shopping_list.models import ShoppingItem

"""
DRF comes with a few serializer types out-of-the-box:
reference: https://www.django-rest-framework.org/api-guide/serializers/

- BaseSerializer
- ModelSerializer
- HyperlinkedModelSerializer
- ListSerializer
"""


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]
