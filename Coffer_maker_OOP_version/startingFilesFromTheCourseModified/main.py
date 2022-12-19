from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

makerOfCoffee = CoffeeMaker()
cashMachine = MoneyMachine()

menuStuff = Menu()

activated = True
while activated:
    drinkChoice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drinkChoice == "report":
        makerOfCoffee.report()
        cashMachine.report()
    elif drinkChoice == "off":
        activated = False
    elif drinkChoice in menuStuff.get_items():
        if makerOfCoffee.is_resource_sufficient(menuStuff.find_drink(drinkChoice)):
            if cashMachine.make_payment(menuStuff.find_drink(drinkChoice).cost):
                makerOfCoffee.make_coffee(menuStuff.find_drink(drinkChoice))
