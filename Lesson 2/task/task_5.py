def check_password():
    _password = "some password"
    print("Please enter your name:")
    client_name = input()
    print("Please enter your password:S")
    client_password = input()

    while client_password != "cancel":
        if client_password == _password:
            print("Password for user: {} is correct".format(client_name))
            break
        else:
            print("Password for user: {} is incorrect".format(client_name))
            print("Please try again...")
        print("Please enter your password: ")
        client_password = input()


if __name__ == "__main__":
    check_password()
