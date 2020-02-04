from website_alive.check_responce import check_URL


print("Enter URL")
URL=input()
if check_URL(URL):
    print("{} is available".format(URL))
else:
    print("{} is not available".format(URL))