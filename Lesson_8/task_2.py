import requests


def exchange(curr: float, orig_curr: str, target_curr: str) -> float:
    orig_curr = orig_curr.upper()
    target_curr = target_curr.upper()
    url = "https://api.exchangerate-api.com/v4/latest/" + orig_curr
    response = requests.get(url)
    data = response.json()
    return curr * data['rates'][target_curr]


print(exchange(100, "rub", "usd"))
