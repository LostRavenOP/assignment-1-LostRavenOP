"""
File: ship.py
Description: Module where the code for the Ship class is written.
Author: Raj Rathod
ID: 1104406560
Username: ratrk002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import Loot class from the loot module, gives access to all it's attributes and methods.
from loot import Loot


# Class to represent a real world Ship object.
class Ship:
    
    # Constructor to define attributes related to the class.
    # Takes name of ship as parameter.
    def __init__(self, name):
        self.__name = name    # Attribute to store the Ship's name.
        self.__damage_counter = 0     # Attribute to store the Ship's damage taken.
        self.__is_broken = False      # Attribute to store the Ship's broken status.
        self.__canon_ball = Loot("Canon Ball", "A projectile used by ancient warriors for battle")      # Attribute to store a canon ball loot object.
        self.__cargo = [self.__canon_ball, self.__canon_ball]     # Attribute to store the ship's cargo.
    

    # Getter for the name of the ship.
    def get_name(self):
        return self.__name

    # Getter for the damage counter of the ship.
    def get_damage_counter(self):
        return self.__damage_counter
    
    # Getter for the broken status of the ship.
    def get_is_broken(self):
        return self.__is_broken
    
    def get_canon_ball(self):
        return self.__canon_ball

    # Getter for the cargo of the ship.
    def get_cargo(self):
        return self.__cargo
    

    # Method to repair Ship.
    def repair_ship(self):

        # If the ship has taken damage and the ship is not broken.
        # Reset the damage counter to 0.
        if self.__damage_counter > 0 and self.__is_broken == False:
            self.__damage_counter = 0
            print(f"{self.__name} has been repaired - good as new!")

        # If the ship is broken, then change the broken status to not broken and reset the damage counter to 0.
        elif self.__is_broken == True:
            self.__is_broken = False
            self.__damage_counter = 0
            print(f"{self.__name} has been repaired - it is no longer broken!")
        else:
            print(f"{self.__name} does not need repairing - come back later!")


    # Method to take a hit on the ship.
    def take_hit(self):

        # Increase the damage counter by 1 each time the ship is hit.
        self.__damage_counter += 1
        print(f"{self.__name} took a hit! Current damage taken: {self.__damage_counter}")

        # Check if the ship is broken (when the damage counter is at 2).
        # If broken, set the broken status to True.
        if self.__damage_counter >= 2:
            self.__is_broken = True
            print(f"{self.__name} is broken - needs to be repaired immediately!")


    # Method to check and return the ship's condition.
    def ship_condition(self):

        # Return a string based on the ship's condition (good, bad, horrible).
        if self.__damage_counter == 0:
            return f"The ship is in EXCELLENT condition."
        elif self.__damage_counter == 1:
            return f"The ship is in GOOD condition."
        elif self.__damage_counter == 2:
            return f"The ship is in HORRIBLE condition."


    # Method to display all the details of the ship including its name, condition, and loot in cargo.
    def __str__(self):

        # Initialize a string variable to store the details of the ship including its name, condition, and cargo items.
        ship_details = f"{self.__name}\nCurrent Condition: {self.ship_condition()}\n\n    --Cargo Items--"

        # Check if the cargo list is empty and print a message if it is, else loop through the cargo list and concatenate a string with each item.
        if len(self.__cargo) == 0:
            ship_details += f"\n   No items in cargo :("
        else:
            for loot in self.__cargo:
                ship_details += "\n" + "- " + str(loot)
        return ship_details


    name = property(get_name)      # Property attribute for the ship name.
    damage_counter = property(get_damage_counter)       # Property attribute for the damage counter.
    is_broken = property(get_is_broken)      # Property attribute for the is_broken state.
    canon_ball = property(get_canon_ball)     # Property attribute for the canon ball loot object.
    cargo = property(get_cargo)     # Property attribute for the cargo.