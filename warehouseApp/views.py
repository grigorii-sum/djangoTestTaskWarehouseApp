import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


@api_view(['POST'])
def warehouse_order_create(request):
    serializer = WarehouseOrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def warehouse_order_update(request, pk):
    required_warehouse_order = WarehouseOrder.objects.get(order_number=pk)
    serializer = WarehouseOrderSerializer(instance=required_warehouse_order, data=request.data)

    if serializer.is_valid():
        serializer.save()

        requests.patch('http://127.0.0.1:8001/store-order/update-from-warehouse/{0}/'.format(pk), data=request.data)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def warehouse_order_update_from_store(request, pk):
    required_warehouse_order = WarehouseOrder.objects.get(order_number=pk)
    serializer = WarehouseOrderSerializer(instance=required_warehouse_order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def warehouse_order_delete(request, pk):
    required_warehouse_order = WarehouseOrder.objects.get(order_number=pk)
    required_warehouse_order.delete()

    requests.delete('http://127.0.0.1:8001/store-order/delete/{0}/'.format(pk))

    return Response('Warehouse Order and Store order were successfully deleted', status=status.HTTP_200_OK)


@api_view(['GET'])
def warehouse_order_detail(request, pk):
    warehouse_order = WarehouseOrder.objects.get(id=pk)
    serializer = WarehouseOrderSerializer(warehouse_order, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

