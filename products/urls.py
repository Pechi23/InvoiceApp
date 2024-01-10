from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list_view),
    path('product-delete/<slug:slug>', views.product_delete_view),
]