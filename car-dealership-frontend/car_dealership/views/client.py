import requests
from urllib.parse import urljoin
from django.shortcuts import render
from .consts import *


def account(request):
    # TODO: client auth
    context = {
        "client": requests.get(urljoin(BASE_URL, "client/1/")).json(),
    }
    return render(request, "account.html", context)
