from website_alive.make_request import call


def check_URL(site):
    responce=call(site)
    if responce.status_code==200:
        return True
    return False