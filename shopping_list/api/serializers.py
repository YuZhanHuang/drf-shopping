from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from shopping_list.models import ShoppingItem

"""
DRF comes with a few serializer types out-of-the-box:
reference: https://www.django-rest-framework.org/api-guide/serializers/

- BaseSerializer
- ModelSerializer
- HyperlinkedModelSerializer
- ListSerializer

Browsable API
check this at http://127.0.0.1:8000/api/shopping-items/

Since we actually don't want the client to be able to create their own UUIDs, 
we can make the id field read-only.
read-only reference: https://www.django-rest-framework.org/api-guide/fields/#read_only

"""


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]
        read_only_fields = ('id',)
        # Here is setting for specific serializer
        # renderer_classes = [JSONRenderer]