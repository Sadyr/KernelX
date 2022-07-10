from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(max_length=150, null=False, blank=True)
    priority = models.PositiveIntegerField(default=0)
    is_for_cart = models.BooleanField(default=False, verbose_name=_('Категория "У кассы"'))

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ("priority", )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "tag"
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ("priority", )

    def __str__(self):
        return self.name


class Items(models.Model):

    name = models.CharField(max_length=150, null=False, blank=True)
    description = models.TextField()
    image = models.ImageField(null=False, upload_to='')
    price = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="items")

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name