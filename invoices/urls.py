from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoices_list_view),
    path('add-to/<slug:slug>', views.invoice_add_view),
    path('delete/<slug:slug>', views.invoice_delete_view),
    path('delete/<slug:invoice_slug>/<slug:invoice_product_slug>', views.invoice_product_delete_view),
    path('<slug:slug>', views.invoice_edit_view),
]