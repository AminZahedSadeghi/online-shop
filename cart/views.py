from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.views import View
from django.contrib import messages

from .cart import Cart
from products.models import Product
from .forms import AddProductToCartForm

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})
    
class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        form = AddProductToCartForm(request.POST)
        product = get_object_or_404(Product, id=product_id)
        
        if form.is_valid():
            cd = form.cleaned_data
            qty = cd['qty']
            cart.add(product, qty)
            messages.success(request, _('Your Product Added To Cart Successfully :) '))
            return redirect('cart:detail')
        

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        cart.remove(product)
        messages.success(request, _('The Product Has Been Removed :)'))
        return redirect('cart:detail')
        
        
            
            