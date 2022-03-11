import classes
import data
from data import poisons_list
from classes import Drink, Store

poison_bar = Store("Poison Bar", "Depths of the virtual world")

for i in poisons_list:
    poison_bar.products_list.append(Drink(**i))

print(f'{poison_bar}\nHere, let me show you the menu:')
poison_bar.menu_printer()
poison_bar.buy_drink()
