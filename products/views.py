from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddProductToCartForm


class ProductListView(generic.ListView):
    # we can use func get_queryset too, but we should add => model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(View):
    form_class = CommentForm
    template_name = 'products/product_detail.html'

    def setup(self, request, *args, **kwargs):
        self.product_instance = Product.objects.get(
            pk=kwargs['product_id'], slug=kwargs['product_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        product = self.product_instance
        comments = Comment.active_comments_and_false_replys.filter(
            product=product)
        comment_form = self.form_class()
        add_to_cart_form = AddProductToCartForm

        return render(request, self.template_name, {'product': product, 'comments': comments, 'comment_form': comment_form, 'add_to_cart_form': add_to_cart_form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        product = self.product_instance
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.product = product
            new_comment.save()
            messages.success(
                request, _('Your Comment Added Successfully :)'))
            return redirect('products:detail', product.id, product.slug)
        else:
            messages.warning(
                request, _('The Information Your Entered Was Not Correct :/'))
            return render(request, self.template_name, {'form': form})


class ReplyView(View):
    @method_decorator(login_required)
    def post(self, request, comment_id, product_id):
        product = Product.objects.get(pk=product_id)
        comment = Comment.objects.get(pk=comment_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.user = request.user
            new_reply.product = product
            new_reply.reply = comment
            new_reply.is_reply = True
            new_reply.save()
            messages.success(
                request, _('Your Reply Added Successfully :)'))
            return redirect('products:detail', product.id, product.slug)
        else:
            messages.warning(
                request, _('The Information Was Not Correct :/'))
            return redirect('products:detail', product.id, product.slug)
