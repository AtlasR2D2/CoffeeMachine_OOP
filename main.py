from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

blnOperational=True
while blnOperational:

    User_Selection = input(f"What would you like? ({menu.get_items()}): ").lower()
    #Process Selection
    if User_Selection == "report":
        coffee_machine.report()
    elif User_Selection == "off":
        blnOperational = False
        print("Powering down coffee machine.")
    else:
        try:
            drink_choice = menu.find_drink(User_Selection)
            if coffee_machine.is_resource_sufficient(drink_choice):
                if money_machine.make_payment(drink_choice.cost):
                    coffee_machine.make_coffee(drink_choice)
                else:
                    print("Sorry that's not enough money. Money refunded.")
        except:
            print("Enter a valid selection.")
