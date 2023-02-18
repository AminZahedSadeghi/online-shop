import urllib.parse

from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Product, Comment
from .forms import CommentForm


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
        comments = Comment.objects.filter(product=product, is_reply=False)
        comment_form = self.form_class()

        return render(request, self.template_name, {'product': product, 'comments': comments, 'comment_form': comment_form})

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
                request, 'کامنت شما با موفقیت ثبت شد :)', 'success')
            return redirect('products:detail', product.id, product.slug)
        else:
            messages.warning(
                request, 'اطلاعات وارد شده صحیح نمیباشد :/', 'warning')
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
            messages.success(request, f'ریپلای شما برای محصول ({product.title}) و کامنت ({comment.body[:30]} ...) اضافه شد', 'success')
            return redirect('products:detail', product.id, product.slug)
        else:
            messages.warning(request, 'اطلاعات وارد شده صحیح نمیباشد :/', 'warning')
            return redirect('products:detail', product.id, product.slug)
                
