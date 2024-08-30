"""
File: pirate.py
Description: Module where the code for the Pirate class is written.
Author: Raj Rathod
ID: 1104406560
Username: ratrk002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import Loot class from the loot module, gives access to all it's attributes and methods.
from loot import Loot


# Class to represent a real world Pirate.
class Pirate:

    # Constructor to define attributes related to the class.
    def __init__(self, name):
        self.__name = name    # Attribute to store the Pirate's name.
        self.__gold_piece = Loot("Gold Piece", "A valueable, round, and gold object that can cause wars")     # Attribute to store a gold piece.
        self.__inventory = [self.__gold_piece]   # Attribute to store items in Pirate's inventory.
        self.__ship_count = 0   # Attribute to count if pirate has a ship.
        self.__ship = None    # Attribute to check if the pirate has a ship.


    # Getter methods for all Pirate attributes
    def get_name(self):
        return self.__name
    
    def get_gold_piece(self):
        return self.__gold_piece
    
    def get_inventory(self):
        return self.__inventory
    
    def get_ship_count(self):
        return self.__ship_count
    
    def get_ship(self):
        return self.__ship
    

    # Method to check if the pirate has a ship.
    def check_ship(self):
        if self.__ship_count == 0 and not (self.__ship_count < 0):
            return False
        else:
            return True


    # Method to check, return and remove an item from the pirate's inventory.
    def retrieve_item(self, item):

        loot_item = False    # Temporary variable to store the item.

        # Check if the item is an instance of Loot and if it is in the pirate's inventory.
        if isinstance(item, Loot) and (item in self.__inventory):
            loot_item = item

            # Remove the item from the pirate's inventory.
            self.__inventory.remove(item)
            return loot_item
        else:
            return loot_item


    # Method to purchase a ship.
    def purchase_ship(self, ship):

        # Check that the pirate doesn't have a ship.
        if self.check_ship() == False:

            # Check that a gold piece is in the inventory.
            # If it is, then remove it from the inventory and assign a ship to the pirate.
            if self.retrieve_item(self.__gold_piece):
                self.__ship_count += 1
                self.__ship = ship
                print(f"{self.__name} has successfully acquaried {self.__ship.name} - make sure to take good care of it!")
            else:
                print(f"{self.__name} does not have enough gold to acquire {self.__ship.name}")

        # If the pirate owns a ship, then check if the pirate has a gold piece to print appropriate message.
        elif self.check_ship() == True:
            if self.retrieve_item(self.__gold_piece):
                print(f"{self.__name} already owns a ship")
            else:
                print(f"Sorry, {self.__name} does not enough gold to buy another ship!")


    # Method to repair the pirate's ship.
    def ship_repair(self):

        # Check if the pirate has a ship and if the ship needs to be repaired.
        if self.check_ship() == True and self.__ship.damage_counter > 0:

            # Check if the pirate has enough gold to repair the ship.
            if self.retrieve_item(self.__gold_piece):

                # Call the repair_ship method from the Ship class.
                self.__ship.repair_ship()
            else:
                print(f"Sorry, {self.__name} does NOT have enough gold to repair the ship :(")

        # Check if the pirate has a ship and if it is in need of repairs.
        elif self.check_ship() == True and self.__ship.damage_counter == 0:
            print(f"{self.__ship.name} is already in EXCELLENT condition!")
        else:
            print(f"Arrgh~ {self.__name} first needs to BUY a ship in order to repair it!")


    # Method to loot a ship.
    def loot_ship(self, opponent_ship):

        # If pirate has a ship, take all loot all loot from enemy ship and add it to pirate's inventory.
        if self.check_ship() == True:
            self.__inventory.extend(opponent_ship.cargo)
            opponent_ship.cargo.clear()


    # Method to fire a canonball at an enemy ship.
    def fire_canonball(self, enemy_ship):

        # Check if pirate has a ship and if the enemy ship has enough damage to be hit.
        if self.check_ship() == True:
            if enemy_ship.damage_counter < 2:

                # If the pirate has a canon ball in their inventory, then remove it and call the take_hit() method for the enemy ship.
                if self.retrieve_item(Loot("Canon Ball", "A projectile used by ancient warriors for battle")):
                    enemy_ship.take_hit()
                else:
                    print(f"{self.__name} can't fire - No Canon Balls on board!")

            # If the enemy ship is destroyed, the pirate loots the enemy ship.
            elif enemy_ship.damage_counter == 2:
                print(f"raagghh!! Time to loot {enemy_ship.name}!")
                self.loot_ship(enemy_ship)
        else:
            print(f"{self.__name} does not own a ship - no canons can be fired!")


    # Method to store an item in the inventory (or all items) to the ships cargo.
    def store_item(self, item=None):

        # If the pirate has a ship and an item is passed through as an argument, then checks if the item is in inventory.
        if self.check_ship() == True:
            if isinstance(item, Loot):
                if item in self.__inventory:

                    # Store the item to cargo.
                    self.__inventory.remove(item)
                    self.__ship.cargo.append(item)
                    print(f"{item.name} has been moved to {self.__ship.name}'s cargo.")
                else:
                    print(f"{item.name} is not in {self.name}'s inventory.")

            # If no arguement is provided, then stores all the items from the inventory to cargo.
            else:
                self.__ship.cargo.extend(self.__inventory)
                self.__inventory.clear()
                print(f"All items have been moved to {self.__name}'s cargo.")
        else:
            print(f"{self.__name} does not own a ship - no cargo to store items in!")


    # Method to retrieve an item from the ships cargo (or all items) to the inventory.
    def retrieve_item_from_cargo(self, item=None):

        # If the pirate has a ship and an item is passed through as an argument, then checks if the item is in cargo.
        if self.check_ship() == True:
            if isinstance(item, Loot):
                if item in self.__ship.cargo:

                    # Retrieve the item to inventory.
                    self.__inventory.append(item)
                    self.__ship.cargo.remove(item)
                    print(f"{item.name} has been moved to {self.__name}'s inventory.")
                else:
                    print(f"{item.name} is not in the cargo.")

            # If no arguement is provided, then retrieves all the items from the cargo to inventory.
            else:
                self.__inventory.extend(self.__ship.cargo)
                self.__ship.cargo.clear()
                print(f"All items have been moved to {self.__name}'s inventory.")
        else:
            print(f"{self.__name} does not own a ship - no cargo to retrieve from!")


    # Method to add a gold piece to the pirate's inventory
    def plus_gold(self):
        self.__inventory.append(self.__gold_piece)


    # String conversion method for the Pirate class.
    def __str__(self):

        # Variable to store a string for the pirate's details.
        pirate_inventory = f"Pirate Name: {self.__name}\nShip: {self.__ship}\n\n    --Items in inventory--\n"

        # If there are no items in inventory, then concatenate a string to indicate it.
        if len(self.__inventory) == 0:
            pirate_inventory += "\n     Inventory is EMPTY!\n"
        else:

            # Loop through the inventory and concatenate a string with each item.
            for loot in self.__inventory:
                pirate_inventory += "\n" + "- " + str(loot)

        # Return the variable.
        return pirate_inventory


    name = property(get_name)   # Property attribute for the name.
    gold_piece = property(get_gold_piece) # Property attribute for gold piece.
    inventory = property(get_inventory)     # Property attribute for the inventory.
    ship_count = property(get_ship_count)   # Property attribute for the ship count.
    ship = property(get_ship)   # Property attribute for the ship.