"""
action decorator

Parameters for the @action decorator:

1. `detail` is the only required parameter. It determines whether this action applies
    to detail requests or list requests.
2. `methods` is a list of HTTP methods that this action responds to. If it's not set, it defaults to the GET method.
3. `url_path` defines the URL segment for this action. If it's not set, it defaults to the name of the method.
4. `url_name` defines the reverse URL name for this action. If it's not set, it's the name of the method;
    underscores are replaced with dashes.
"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shopping_list.api.serializers import ShoppingItemSerializer
from shopping_list.models import ShoppingItem


class ShoppingItemViewSet(ModelViewSet):
    queryset = ShoppingItem.objects.all()  # noqa
    serializer_class = ShoppingItemSerializer

    @action(detail=False, methods=['DELETE'], url_path='delete-all-purchased', url_name='delete-all-purchased')
    def delete_purchased(self, request):
        ShoppingItem.objects.filter(purchased=True).delete()  # noqa

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['PATCH'], url_path='mark-bulk-purchased', url_name='mark-bulk-purchased')
    def mark_bulk_purchased(self, request):
        try:
            queryset = ShoppingItem.objects.filter(id__in=request.data['shopping_items'])  # noqa
            queryset.update(purchased=True)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
