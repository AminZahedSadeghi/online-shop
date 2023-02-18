from django.db import models
from django.shortcuts import reverse

from accounts.models import CustomUser


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


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomments')
    is_reply = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.product}'
