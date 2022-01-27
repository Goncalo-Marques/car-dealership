from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from urllib.parse import urljoin
from django.shortcuts import render
from .consts import *
from car_dealership import models


def register(request):
    form = models.ClientForm(request.POST or None)
    if form.is_valid():
        response = requests.post(
            urljoin(BASE_URL, "auth/register/"),
            data=form.data,
            cookies=request.COOKIES,
            headers={"X-CSRFToken": request.COOKIES.get("csrftoken")},
        )

        if response.status_code == 201:
            CLIENT = response.json().get("client")
            print("111111: " + str(CLIENT))
            redirect = HttpResponseRedirect(reverse("index"))
            return redirect
        else:
            return render(request, "error.html", response.json())

    return render(request, "register.html")


def account(request):
    # TODO: client auth
    context = {
        "client": requests.get(urljoin(BASE_URL, "client/1/")).json(),
    }
    return render(request, "account.html", context)
