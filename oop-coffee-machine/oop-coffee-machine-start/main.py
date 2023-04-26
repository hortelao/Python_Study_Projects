from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        machine.report()
        money.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)


