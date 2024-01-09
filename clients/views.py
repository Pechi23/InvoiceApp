from django.shortcuts import render
from .models import Client
# Create your views here.

def clients_list_view(request):
    clients = Client.objects.all()
    context = {
        "clients": clients,
    }
    return render(request, "clients-list.html", context=context)
