from django.urls import path, re_path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    re_path(r'(?P<product_id>[\d+])/(?P<product_slug>[-\w]+)/', views.ProductDetailView.as_view(), name='detail'),
]
