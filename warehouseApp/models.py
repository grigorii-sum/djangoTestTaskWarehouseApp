from django.db import models


class WarehouseOrder(models.Model):
    order_number = models.CharField(max_length=100)
    STATUS_TYPES = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Stored', 'Stored'),
        ('Send', 'Send')
    )
    order_status = models.CharField(max_length=11, choices=STATUS_TYPES)
    store_account = models.CharField(max_length=3)

    def __str__(self):
        return 'STORE "{0}" HAS ORDER "{1}" WITH STATUS = {2}'.format(self.store_account, self.order_number, self.order_status)

