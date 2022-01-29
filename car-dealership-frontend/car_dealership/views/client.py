from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urljoin
from django.shortcuts import render
from . import helpers
from .consts import (
    TEMPLATE_ACCOUNT,
    TEMPLATE_ERROR,
    TEMPLATE_LOG_IN,
    TEMPLATE_SIGN_UP,
    URL_INDEX,
)
from car_dealership import models


def logIn(request):
    form = models.ClientLoginForm(request.POST or None)
    if form.is_valid():
        response = helpers.post("auth/login/", request.COOKIES, form.data)
        if response.status_code != 200:
            return render(request, TEMPLATE_ERROR, response.json())

        redirect = HttpResponseRedirect(reverse(URL_INDEX))
        if response.cookies.get("sessionid") != None:
            redirect.set_cookie("sessionid", response.cookies.get("sessionid"))
            redirect.set_cookie("client", response.json().get("client", None))

        return redirect

    return render(request, TEMPLATE_LOG_IN)


def signUp(request):
    form = models.ClientRegisterForm(request.POST or None)
    if form.is_valid():
        response = helpers.post("auth/register/", request.COOKIES, form.data)
        if response.status_code != 201:
            return render(request, TEMPLATE_ERROR, response.json())

        redirect = HttpResponseRedirect(reverse(URL_INDEX))
        if response.cookies.get("sessionid") != None:
            redirect.set_cookie("sessionid", response.cookies.get("sessionid"))
            redirect.set_cookie("client", response.json().get("client", None))

        return redirect

    return render(request, TEMPLATE_SIGN_UP)


def logOut(request):
    response = helpers.post("auth/logout/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    redirect = HttpResponseRedirect(reverse(URL_INDEX))
    redirect.delete_cookie("sessionid")
    redirect.delete_cookie("client")

    return redirect


def account(request):
    client = helpers.get_client_or_none(request)

    form = models.ClientAccountForm(request.POST or None)
    if form.is_valid():
        clientID = client.get("id", None)
        response = helpers.put(f"client/{clientID}/", request.COOKIES, form.data)
        if response.status_code != 200:
            return render(request, TEMPLATE_ERROR, response.json())

        redirect = HttpResponseRedirect(reverse(URL_INDEX))
        redirect.set_cookie("client", response.json())

        return redirect

    context = {
        "client": client,
    }
    return render(request, TEMPLATE_ACCOUNT, context)
