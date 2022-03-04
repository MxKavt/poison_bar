poisons_list = [
    {"id": 1,
     "name": "Vtopia",
     "model": "Long Drink",
     "recipe": "Grapefruit juice, mango juice, brown sugar, blue kurasao, tonic water, blueberry gin",
     "price": 24,
     "quantity": "3"},
    {"id": 2,
     "name": "Hard-boiled Cop",
     "model": "Short Drink",
     "recipe": "Scotch, lime juice, brown sugar, ice ball",
     "price": 25,
     "quantity": 5},
    {"id": 3,
     "name": "Night City Blues",
     "model": "Short Drink",
     "recipe": "Bourbon, coconut, honey, ice ball",
     "price": 27,
     "quantity": 7}
]


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
            var1 = self.check_quantity(chosen_quantity)
            var2 = self.decrease_quantity(var1)
            return var1, var2


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
        pass

    def buy_drink(self):
        first_choice = input("Would you like to buy a drink? Reply Y for yes and N for no: ")
        if first_choice.lower() == "y":
            chosen_drink = self.get_drink_by_id()
            price = chosen_drink[0].price
            chosen_quantity = chosen_drink[1]
            bill = float(price) * float(chosen_quantity)
            print(f"Here's your bill: {chosen_quantity} {chosen_drink[0].name} ${bill}")
        else:
            print("Thank you for visiting, goodbye.")


poison_bar = Store("Poison Bar", "Depths of the virtual world")

for i in poisons_list:
    poison_bar.products_list.append(Drink(**i))

print(f'{poison_bar}\nHere, let me show you the menu:')
poison_bar.menu_printer()
poison_bar.buy_drink()
