from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from apps.nomenclature.models import Items


class PaymentType(models.TextChoices):
    by_cart = ('By card on delivery', '')
    by_cash = ('By cash on delivery', '')


class CartProductQueryset(QuerySet):

    def items(self):
        return self.all()

    @property
    def items_price(self):
        return sum([item.total_price for item in self.cart_items.all()])

    @property
    def total_price(self):
        total_price = self.items_price

        return total_price


class Cart(models.Model):

    @property
    def total_price(self):
        total_price = self.items_price

        return total_price

    @property
    def items(self):
        return self.cart_items.items()

    @property
    def items_count(self):
        if self.cart_items.exists():
            return self.cart_items.all().count()
        return 0

    @property
    def items_price(self):
        return sum([item.total_price for item in self.cart_items.all()])

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'


class CartItems(models.Model):
    item = models.ForeignKey(
        Items,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="cart_items"
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="cart_items"
    )
    count = models.IntegerField(default=1)
    objects = CartProductQueryset.as_manager()

    @property
    def price(self):
        return self.item.price

    @property
    def total_price(self):
        return int(self.count * (self.price or 0))




class DeliveryType(models.TextChoices):
    take_away = ('Take away', '')
    delivery = ('Delivery', '')


class Delivery(models.Model):
    delivery_type = models.CharField(max_length=200, choices=DeliveryType.choices, default=DeliveryType.delivery)
    timeslot = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'


class Order(models.Model):

    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=False, blank=True)
    address = models.TextField()
    total_price = models.PositiveIntegerField()
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, null=True, blank=True)
    payment_type = models.CharField(max_length=200, choices=PaymentType.choices, default=PaymentType.by_cart)

    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"