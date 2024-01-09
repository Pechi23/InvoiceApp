from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email"]

    def clean(self):
        data = self.cleaned_data

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        qs_name = Client.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name)
        if qs_name.exists():
            self.add_error("first_name", f"\"{first_name} {last_name}\" is already registered as a client")

        email = data.get("email")
        qs_email = Client.objects.filter(email__iexact=email)
        if qs_email.exists():
            self.add_error("email", f"\"{email}\" is already used by another client")

        return data