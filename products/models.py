from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('product_detail', args=[self.pk])

