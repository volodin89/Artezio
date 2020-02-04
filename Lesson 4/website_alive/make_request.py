import requests


def call(site):
    responce=requests.get(site)
    return responce