from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)

    @property
    def product_price(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        _items = Basket.objects.filter(user=self.user)
        _total_price = 0
        for _item in _items:
            _total_price += _item.product.price * _item.quantity
        return _total_price
