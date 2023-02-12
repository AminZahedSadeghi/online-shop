from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.id}'

    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id, self.slug])
