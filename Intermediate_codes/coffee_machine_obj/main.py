from Intermediate_codes.coffee_machine_obj.menu import Menu, MenuItem
from Intermediate_codes.coffee_machine_obj.coffee_maker import CoffeeMaker
from Intermediate_codes.coffee_machine_obj.money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


should_continue = True
while should_continue:
    choice = input(f"What would you like? {menu.get_items()}:")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # cost = menu_item.cost
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

