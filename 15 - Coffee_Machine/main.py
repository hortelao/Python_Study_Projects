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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True


def check_resources(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry, we are out of {i}")
            return False
        else:
            return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def process_payment(payment, cost):
    if payment > cost:
        payback = payment - cost
        print(f"Here is ${payback:.2f} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(choice, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


while machine_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    elif choice not in MENU:
        print("Wrong input, please try again.")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if process_payment(payment, drink['cost']):
                make_drink(choice, drink['ingredients'])

