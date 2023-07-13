import os  # Tracking the File location
import json
import pandas # for the usage of the data frame

# Constant
save_file = "container.json"


class Menu:
    def __init__(self):
        self.account = None
        self.prices = None
        self.names = None
        self.data_items = []
        self.pricing = []
        self.quantities = []
        self.data_adding()

    # self.showing_menu()

    def data_adding(self):
        for i in range(int(input("Enter the amount: "))):
            self.names = input("Enter the name of the product: ")
            self.prices = int(input("Enter the price of the items: "))
            self.account = int(input("Enter the amount of the items: "))
            self.data_items.append(self.names)
            self.pricing.append(self.prices)
            self.quantities.append(self.account)

        # TODO Make the protection for refreshing the data in Json
        # Implementation of the error handling
        if os.path.exists(save_file) and os.path.getsize(save_file) > 0:
            with open("container.json", "r") as file:
                try:
                    data_processing = json.load(file)
                except json.decoder.JSONDecodeError as e:
                    print("Error decoding JSON data:", e)
        else:
            data_processing = {}
            # Creating the nested dictionary with looping

        for naming in range(len(self.data_items)):
            fee = self.pricing[naming]
            quanty = self.quantities[naming]
            new_menu = {
                "price": fee,
                "qty": quanty
            }
            data_processing[self.data_items[naming]] = new_menu
            print(data_processing)

        # formatting the Json File
        with open("container.json", "w") as file:
            json.dump(data_processing, file, indent=4)


def showing_menu():
    with open("container.json", "r") as file:
        data = json.load(file)
        menu_df = pandas.DataFrame(data)
        print(menu_df)
