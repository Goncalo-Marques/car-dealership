from django.db import models
from django import forms

# client model
class Client(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)
    full_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, null=False)


# client registration form
class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


# client login form
class ClientLoginForm(forms.ModelForm):
    full_name = forms.CharField(required=False)
    birthdate = forms.DateField(required=False)
    phone_number = forms.IntegerField(required=False)
    address = forms.CharField(required=False)

    class Meta:
        model = Client
        fields = "__all__"


# client details editing form
class ClientAccountForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    password = forms.CharField(required=False)

    class Meta:
        model = Client
        fields = "__all__"
