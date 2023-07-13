import json
from menu import showing_menu
from menu import Menu


class Admin:
    def __init__(self):
        self.item_to_remove = None
        self.search_key = None
        self.operation_choice()
        self.add = None
        self.item = None
        self.data = None
        self.found_item = None
        self.key_point = None

    def operation_choice(self):
        condition = True
        while condition:
            showing_menu()
            match input("1.Adding \n 2.Searching \n 3.Removing \n If you want to quit , click q, \n Choice is : "):
                case '1':
                    self.adding_dat()
                case '2':
                    self.searching_data()
                case '3':
                    self.removing_data()
                case 'q':
                    condition = False
                case _:
                    print("Invalid Operation")

    def adding_dat(self):
        self.add = Menu()

    def searching_data(self):
        self.item = input("Enter the item : ")
        with open("container.json", "r") as file:
            self.data = json.load(file)

        for key in self.data:
            if key == self.item:
                self.found_item = self.data[key]
                print("Item is Found !")
                self.key_point = input("Enter the category : price or qty ")
                if self.key_point in self.found_item:
                    print(self.found_item[self.key_point])
                    break
                else:
                    print("Not found")

    def removing_data(self):
        self.item_to_remove = input("Enter the item to remove: ")
        with open("container.json", "r") as file:
            data = json.load(file)

        if self.item_to_remove in data:
            del data[self.item_to_remove]

            with open("container.json", "w") as file:
                json.dump(data, file)

            print("Item removed successfully.")
        else:
            print("Item not found.")
