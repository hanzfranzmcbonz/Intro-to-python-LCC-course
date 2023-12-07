# Creates a class called Pet.
class Pet:
    
    # Initializes the atributes of Pet.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    # assigns the value of name to the name field
    def set_name(self, name):
        self.__name = name
    
    # Assigns the value of animal type to the animal type field
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    # Assigns the value of age to the age field
    def set_age(self, age):
        self.__age = age
    
    # This method returns value of __name field
    def get_name(self):
        return self.__name
    
    # This method returns the value of __animal type field
    def get_animal_type(self):
        return self.__animal_type
    
    # This method returns the value of __age field
    def get_age(self):
        return self.__age
    
    