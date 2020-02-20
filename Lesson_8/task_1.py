import requests


def size_html():
    response = requests.get("https://google.com")
    return len(response.text)


print(size_html())
