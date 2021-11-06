from django.urls import path

from .views import (
    warehouse_order_create,
    warehouse_order_update,
    warehouse_order_update_from_store,
    warehouse_order_delete,
    warehouse_order_detail
)

urlpatterns = [
    path('create/', warehouse_order_create, name="warehouse-order-create"),
    path('update/<str:pk>/', warehouse_order_update, name="warehouse-order-update"),
    path('update-from-store/<str:pk>/', warehouse_order_update_from_store, name="warehouse-order-update-from-store"),
    path('delete/<str:pk>/', warehouse_order_delete, name="warehouse-order-delete"),
    path('detail/<str:pk>/', warehouse_order_detail, name="warehouse-order-detail"),
]