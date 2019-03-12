from django.urls import path
from .views import (
    product_detail_view, 
    product_create_view,
    dynamic_lookup_view,
    delete_product,
    product_list_view,
    product_update_view
    )

app_name = "products"
urlpatterns = [
    path("create/", product_create_view, name="product_create"),
    path("<int:id>/", dynamic_lookup_view, name='product_detail'),
    path("<int:id>/delete", delete_product, name='product_delete'),
    path("<int:id>/update", product_update_view, name="product_update"),
    path("", product_list_view, name="all_product_lists"),
]