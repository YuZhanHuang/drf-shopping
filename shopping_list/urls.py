"""
DRF provides two possible routers:
1. SimpleRouter
    - reference: https://www.django-rest-framework.org/api-guide/routers/#simplerouter
2. DefaultRouter
    - reference: https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    
Since the DefaultRouter includes a default API root view, making it easier to navigate the Browsable API, 
we'll use this one.    

Browsable API reference:
https://www.django-rest-framework.org/topics/browsable-api/


The register() method has three arguments:

1. prefix (required) - URL prefix for the ViewSet
2. viewset (required) - The ViewSet class
3. basename (optional) - The base to use for the URL names
While the basename is generated by default from the QuerySet,
it's a good idea to be explicit and define it for clarity purposes.
"""

from django.urls import path
from shopping_list.api.views import ListAddShoppingList, ShoppingListDetail, AddShoppingItem, ShoppingItemDetail


urlpatterns = [
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all_shopping_lists"),
    path("api/shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping_list_detail"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", AddShoppingItem.as_view(), name="add-shopping-item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(),
         name="shopping-item-detail"),
]
