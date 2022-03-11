class Drink:
    def __init__(self, id, name, model, recipe, price, quantity):
        self.id = id
        self.name = name
        self.model = model
        self.recipe = recipe
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.id} - {self.name} - {self.model} - ${self.price} - {self.quantity} left'

    def check_quantity(self, chosen_quantity):
        while str(chosen_quantity) > str(self.quantity):
            chosen_quantity = input("too much bro")
        else:
            return chosen_quantity

    def increase_quantity(self):
        pass

    def decrease_quantity(self, var1):
        self.quantity = int(self.quantity) - int(var1)
        return self.quantity

    def sell_drink(self):
        chosen_quantity = input("How many? ")
        while chosen_quantity.isdigit() is False:
            chosen_quantity = input("Make sure you type digits! ")
        else:
            checked_quantity = self.check_quantity(chosen_quantity)
            decreased_quantity = self.decrease_quantity(int(checked_quantity))
            return checked_quantity, decreased_quantity


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products_list = []

    def __repr__(self):
        return f'Welcome to {self.name}, located in the {self.address}!'

    def menu_printer(self):
        for p in self.products_list:
            print(p)

    def get_drink_by_id(self):
        choice = input("Choose the drink by ID: ")
        menu = self.products_list
        while choice > str(len(menu)):
            self.menu_printer()
            choice = input("Wrong ID, try again: ")
        else:
            for drink in menu:
                if choice in str(drink.id):
                    sold_drink = drink.sell_drink()
                    return drink, sold_drink[0], sold_drink[1]

    def add_drink(self):
        pass

    def remove_drink(self):
        e = self.products_list
        for i in e:
            if int(i.quantity) <= 0:
                self.products_list.remove(i)
                return e

    def buy_drink(self):
        first_choice = input("Would you like to buy a drink? Reply Y for yes and N for no: ")
        if first_choice.lower() == "y":
            chosen_drink = self.get_drink_by_id()
            price = chosen_drink[0].price
            chosen_quantity = chosen_drink[1]
            bill = float(price) * float(chosen_quantity)
            print(f"Here's your bill: {chosen_quantity} {chosen_drink[0].name}(s) ${bill}")
            self.remove_drink()
        else:
            print("Thank you for visiting, goodbye.")
