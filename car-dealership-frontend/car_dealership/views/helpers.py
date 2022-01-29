import ast
from urllib.parse import urljoin
import requests
from .consts import BASE_URL

# get request with the necessary cookies to authenticate
def get(url, cookies, data=None):
    headers = {}
    token = cookies.get("csrftoken", None)
    if token != None:
        headers["X-CSRFToken"] = token

    return requests.get(
        urljoin(BASE_URL, url),
        data=data,
        cookies=cookies,
        headers=headers,
    )


# post request with the necessary cookies to authenticate
def post(url, cookies, data=None):
    headers = {}
    token = cookies.get("csrftoken", None)
    if token != None:
        headers["X-CSRFToken"] = token

    return requests.post(
        urljoin(BASE_URL, url),
        data=data,
        cookies=cookies,
        headers=headers,
    )


# put request with the necessary cookies to authenticate
def put(url, cookies, data=None):
    headers = {}
    token = cookies.get("csrftoken", None)
    if token != None:
        headers["X-CSRFToken"] = token

    return requests.put(
        urljoin(BASE_URL, url),
        data=data,
        cookies=cookies,
        headers=headers,
    )


# gets the client cookie or none if it does not exists
def get_client_or_none(request):
    client = request.COOKIES.get("client", None)
    if client != None:
        client = ast.literal_eval(client)

    return client
