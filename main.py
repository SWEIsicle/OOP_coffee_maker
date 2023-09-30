from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects of the classes.
coffee_menu = Menu()
kuerig = CoffeeMaker()
ATM = MoneyMachine()

on = True
""" First, ask the user what would they like.
    The while loop makes the terminal consistently ask for orders unless the machine is told "off".
    Entering 'report' or 'Report' will display the resources left, and money earned.
    Entering a drink name will prompt for payment, and if sufficient, return your order and change."""
while on:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        on = False
        quit()
    elif order == "report" or order == "Report":
        kuerig.report()
        ATM.report()
    else:
        drink = Menu.find_drink(coffee_menu, order_name=order)
        if kuerig.is_resource_sufficient(coffee_menu.find_drink(order_name=order)):
            if ATM.make_payment(drink.cost):
                kuerig.make_coffee(drink)
