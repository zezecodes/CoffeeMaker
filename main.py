from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker 
from money_machine import MoneyMachine

machine = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

machine_on = True

machine.report()
maker.report()

while machine_on:
    options = menu.get_items()
    order = input(f"What would you like to order? - ({options}) : ")
    if order == "off":
        machine_on = False
    elif order == "report":
        maker.report()
        machine.report()
    else:
        drink = menu.find_drink(order)
        is_enough_ingredients = maker.is_resource_sufficient(drink)
        is_payment_successful = machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            maker.make_coffee(drink) 