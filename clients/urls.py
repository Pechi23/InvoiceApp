from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list_view),
    path('client-delete/<slug:slug>', views.client_delete_view),
]