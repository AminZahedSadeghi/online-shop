from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', allow_unicode=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
