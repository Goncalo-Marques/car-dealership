from typing_extensions import Required
from django.db import models
from django import forms


class Client(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)
    full_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, null=False)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
