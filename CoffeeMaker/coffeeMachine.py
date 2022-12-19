MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
activated = True
while activated:
    drinkChoice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drinkChoice == "report":
        print(f'''
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${resources["money"]}
        ''')
    elif drinkChoice == "off":
        activated = False

    elif drinkChoice in list(MENU.keys()):
        print("Please insert coins.")
        noOfQuarters = float(input("How many quarters?: "))
        noOfDimes = float(input("How many dimes?: "))
        noOfNickles = float(input("How many nickles?: "))
        noOfPennies = float(input("How many pennies?: "))
        cost = noOfPennies * 0.01 + noOfDimes * 0.1 + noOfQuarters * 0.25 + noOfNickles * 0.05
        if cost >= MENU[drinkChoice]["cost"]:
            if resources["water"] >= MENU[drinkChoice]["ingredients"]["water"] and resources["milk"] >= MENU[drinkChoice]["ingredients"]["milk"] and resources["coffee"] >= MENU[drinkChoice]["ingredients"]["coffee"]:
                print(f"Here is your {drinkChoice} ☕️. Enjoy!")
                print(f'Here is ${cost - MENU[drinkChoice]["cost"]} in change.')

                # Update the resources list
                resources["water"] -= MENU[drinkChoice]["ingredients"]["water"]
                resources["milk"] -= MENU[drinkChoice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[drinkChoice]["ingredients"]["coffee"]
                resources["money"] += MENU[drinkChoice]["cost"]
            else:
                if resources["water"] < MENU[drinkChoice]["ingredients"]["water"]:
                    print("Sorry there is not enough water.")
                elif resources["milk"] < MENU[drinkChoice]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk.")
                elif resources["coffee"] < MENU[drinkChoice]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee.")
        else:
            print("Sorry that's not enough money. Money refunded.")

# Penny = 1 cent
# Dime = 10 cent
# Nickel = 5 cent
# Quarter = 25 cent
