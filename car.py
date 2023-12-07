# Creates a class called Car
class Car:
    
    # Initializes the arguments
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    # Adds 5 speed when called
    def accelerate(self):
        self.__speed += 5
    
    # subtracts 5 speed when called
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
    
    # Gets Speed 
    def get_speed(self):
        return self.__speed
