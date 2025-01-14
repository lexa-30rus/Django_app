from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')

    def get_absolute_url(self):
        return reverse('shopapp:product_details', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Product (pk={self.pk}, name={self.name})"


class Order(models.Model):
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    product = models.ManyToManyField(Product, related_name="orders")

    def __str__(self):
        return f"Product (pk={self.pk}, user={self.user})"
