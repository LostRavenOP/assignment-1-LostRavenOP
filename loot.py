"""
File: loot.py
Description: Module where the code for the Loot class is written.
Author: Raj Rathod
ID: 1104406560
Username: ratrk002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Class to represent a real world Loot object.
class Loot:

    # Constructor to define attributes related to the class.
    # Takes name and description of the Loot as the parameter.
    def __init__(self, name, description):
        self.__name = name      # Private attribute to store the loot name.
        self.__description = description    # Private attribute to store the loot description.


    # Getter to access the Loot name from outside the Loot class.
    def get_name(self):
        return self.__name
    
    # Getter to access the Loot description from outside the Loot class.
    def get_description(self):
        return self.__description

    # String Conversion method to display the name and description of the Loot object.
    def __str__(self):
        return f"{self.__name}: {self.__description}"
    

    # Method to compare two Loot objects based on their names and descriptions.
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Loot):
            return self.__name == value.name and self.__description == value.description
        else:
            return False
            
    name = property(get_name)     # Property attribute for the name.
    description = property(get_description)    # Property attribute for the description.