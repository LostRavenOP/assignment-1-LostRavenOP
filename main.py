"""
File: main.py
Description: Module where the main code is written and executed.
Author: Raj Rathod
ID: 1104406560
Username: ratrk002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import Pirate, Ship, and Loot classes from their respective modules
# Gives access to all their attributes and methods.
from pirate import Pirate
from ship import Ship
from loot import Loot

# Create instances of Ship and Pirate Classes
going_merry = Ship("The Going Merry")
luffy = Pirate("Monkey.D.Luffy")
thousand_sunny = Ship("The Thousand Sunny")
zoro = Pirate("Roronoa Zoro")

print("------------------------------------------")
print(f"----- Let The Grand Adventure Begin! -----")
print("------------------------------------------")

# Print initial state of pirate 'Luffy'
print(luffy)
print("------------------------------------------")

# Luffy purchases a ship
luffy.purchase_ship(going_merry)
print("------------------------------------------")

# Print state of pirate 'Luffy' after purchasing a ship
print(luffy)
print("------------------------------------------")

# Print initial state of pirate 'Zoro'
print(zoro)
print("------------------------------------------")

# Zoro tries to purchase a ship multiple times
zoro.purchase_ship(thousand_sunny)
print("------------------------------------------")
zoro.purchase_ship(thousand_sunny)
print("------------------------------------------")

# Print state of pirate 'Zoro' after purchasing a ship
print(zoro)
print("------------------------------------------")

# Luffy fires canon ball at Zoro's ship
luffy.fire_canonball(zoro.ship)
print("------------------------------------------")

# Luffy retrieves a canon ball from his ship
luffy.retrieve_item_from_cargo(Loot("Canon Ball", "A projectile used by ancient warriors for battle"))
print("------------------------------------------")

# Luffy fires canon ball at Zoro's ship again
luffy.fire_canonball(zoro.ship)
print("------------------------------------------")

# Luffy tries to retrieve the rest of the items from his ship
# Fires another canon ball at Zoro's ship
luffy.retrieve_item_from_cargo()
luffy.fire_canonball(zoro.ship)
print("------------------------------------------")

# Zoro tries to repair his ship
zoro.ship_repair()
print("------------------------------------------")

# Zoro is given gold (for testing purposes) and attempts to repair again
zoro.plus_gold()
zoro.ship_repair()
print("------------------------------------------")

# Zoro is given gold and tries to repair again
zoro.plus_gold()
zoro.ship_repair()
print("------------------------------------------")

# Zoro tries to retrieve the rest of the items from his ship
# Fires another canon ball at Luffy's ship
zoro.retrieve_item_from_cargo()
zoro.fire_canonball(luffy.ship)
zoro.fire_canonball(luffy.ship)
print("------------------------------------------")

# Luffy is given gold tries to store all items in his ship's cargo
luffy.plus_gold()
luffy.store_item()
print("------------------------------------------")

# Zoro loots Luffy's ship
zoro.fire_canonball(luffy.ship)
print("------------------------------------------")

# Print final states of both pirates
print(luffy)
print("------------------------------------------")
print(zoro)
print("------------------------------------------")