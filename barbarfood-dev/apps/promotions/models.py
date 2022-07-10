from django.db import models


class Promotion(models.Model):
    image = models.ImageField(upload_to='', null=False)
    priority = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'promotions'
        verbose_name = 'Promotions'
        verbose_name_plural = 'Promotions and news'