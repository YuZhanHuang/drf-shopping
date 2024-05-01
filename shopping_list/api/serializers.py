from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from shopping_list.models import ShoppingItem, ShoppingList

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

    def create(self, validated_data, **kwargs):
        """
        This is the self.context['request'].parser_context
        {
            'view': <shopping_list.api.views.AddShoppingItem object at 0x10bb94c10>,
            'args': (),
            'kwargs': {
                'pk': UUID('f0288d88-d7c5-4cf0-a89b-14c9bb7d0454')
                },
            'request':
                <rest_framework.request.Request: POST '/api/shopping-lists/f0288d88-d7c5-4cf0-a89b-14c9bb7d0454/shopping-items/'>,
            'encoding': 'utf-8'
        }
        :param validated_data:
        :param kwargs:
        :return:
        """
        validated_data['shopping_list_id'] = self.context['request'].parser_context['kwargs']['pk']
        return super(ShoppingItemSerializer, self).create(validated_data)


class ShoppingListSerializer(serializers.ModelSerializer):
    shopping_items = ShoppingItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'shopping_items']
