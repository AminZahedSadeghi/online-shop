import urllib.parse

from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)  # we can use func get_queryset too, but we should add => model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['product_id'], slug=self.kwargs['product_slug'])

