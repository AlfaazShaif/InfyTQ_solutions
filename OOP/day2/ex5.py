class Car:
    def __init__(self):
        self.__mileage = None
        self.__fuel_left = None
        self.__initial_fuel = None

    def get_mileage(self):
        return self.__mileage
    def set_mileage(self,mileage):
        self.__mileage = mileage
    
    def get_fuel_left(self):
        return self.__fuel_left
    def set_fuel_left(self,fuel_left):
        self.__fuel_left = fuel_left
    
    def get_initial_fuel(self):
        return self.__initial_fuel
    def set_initial_fuel(self,initial_fuel):
        self.__initial_fuel = initial_fuel
    
    def identify_distance_that_can_be_travelled(self):
        if self.__initial_fuel > 5:
            self.__fuel_left = self.__initial_fuel - 5
            return (self.__initial_fuel - 5) * self.__mileage
        else:
            return 0

    def identify_distance_travelled(self,initial_fuel):


