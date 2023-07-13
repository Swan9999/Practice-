import json

with open("container.json", "r") as file:
    data = json.load(file)

ordered_item = []


def searching_data_client(item):
    for key in data:
        if key == item:
            found_item = data[key]
            print("Item is found:", found_item)
            return found_item


def ordering():
    food = input("Enter the Food name: ")
    quantity = int(input("Enter the amount of the food: "))
    new_food = searching_data_client(food)
    ordered = new_food.copy()
    ordered["qty"] = quantity
    ordered_item.append(ordered)
    print(ordered_item)
    pay_process = input("Did you completed:? Y/N ").lower()
    if pay_process == "y":
        payment()
        data[food]['qty']-= quantity
        print(data[food]['qty'])

    if pay_process == "n":
        ordering()


def payment():
    if (len(ordered_item)) == 0:
        print("You did not choose anything. Are you sure? Y/N")

    final_price = 0
    for objects in ordered_item:
        current_price = objects["price"] * objects["qty"]
        final_price = final_price + current_price

    print(f"Total Price : {final_price}")

    cash = int(input("Enter the Cash: "))
    if cash > final_price:
        return_cash = cash - final_price
        print(f"Return Payement{return_cash}")
        print("Your process is completed thanks you !")

