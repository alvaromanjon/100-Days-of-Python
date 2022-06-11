MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

input_str = ""


def report_screen():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_resources(type_coffee):
    check = True

    for i in MENU[type_coffee]["ingredients"].keys():
        if MENU[type_coffee]["ingredients"][i] > resources[i]:
            check = False
            ingredient = i

    if not check:
        print(f"Sorry, there is not enough {ingredient}")
    return check


def process_coins():
    print("Please insert coins.")
    dimes = int(input("How many dimes?: "))
    nickes = int(input("How many nickes?: "))
    pennies = int(input("How many pennies?: "))
    quarters = int(input("How many quarters?: "))

    cash = 0.25 * dimes + 0.1 * nickes + 0.05 * pennies + 0.01 * quarters
    print(f"Money inserted: ${cash}")
    return cash


def check_transaction(cash, type_coffee):
    if cash < MENU[type_coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cash > MENU[type_coffee]["cost"]:
        exchange = cash - MENU[type_coffee]["cost"]
        print("Here is ${:0.2f} dollars in change.".format(exchange))
        cash -= exchange
    resources["money"] += cash
    return True


def make_coffee(type_coffee):
    if not check_resources(type_coffee):
        return

    cash = process_coins()
    if not check_transaction(cash, type_coffee):
        return

    for i in MENU[type_coffee]["ingredients"].keys():
        resources[i] -= MENU[type_coffee]["ingredients"][i]

    print("Here is your latte. Enjoy!")


while input_str != "off":
    input_str = input("What would you like? (espresso/latte/cappuccino): ")
    if input_str == "report":
        report_screen()
    for key in MENU.keys():
        if input_str == key:
            make_coffee(input_str)
