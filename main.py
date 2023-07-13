import admin
import client
from menu import showing_menu
save_file = "container.json"


def determination_user():
    user = input("Admin/ User? ").lower()
    if user == "admin":
         admin.Admin()
    elif user == "user":
        showing_menu()
        option = input("Do You want to order ? Y/N").lower()
        if option == "y":
            client.ordering()
        elif option == "n":
            print("Thanks for joining our application")
    else:
        print("Invalid User, Choose the Valid User ")
        determination_user() # the Recursion


determination_user()
