from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

input_str = ""

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while input_str != "off":
    input_str = input(f"What would you like? ({menu.get_items()}): ")
    if input_str == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(input_str)
        if coffee is not None:
            if coffee_machine.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_machine.make_coffee(coffee)

