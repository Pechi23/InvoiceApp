from django.shortcuts import render
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def clients_list_view(request):
    form = ClientForm(request.POST or None)
    clients = Client.objects.filter(user=request.user)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ClientForm()

    context = {
        "clients": clients,
        "form": form,
    }

    return render(request, "clients/clients-list.html", context=context)
