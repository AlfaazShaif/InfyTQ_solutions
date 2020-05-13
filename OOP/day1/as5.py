#OOPR-Assgn-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None

    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id = vehicle_id
    
    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type = vehicle_type
    
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost = vehicle_cost
    
    def get_premium_amount(self):
        return self.__premium_amount
    def set_premium_amount(self,premium_amount):
        self.__premium_amount = premium_amount
    
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.02
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.06
        else:
            print("Invalid Vehicle Type")

    def display_vehicle_details(self):
        print("Vehicle ID : " + str(self.__vehicle_id))
        print("Vehicle Type : " + str(self.__vehicle_type))
        print("Vehicle Cost : " + str(self.__vehicle_cost))
        print("Primum Amont : " + str(self.__premium_amount) + "\n")

maruti_swift = Vehicle()
maruti_swift.set_vehicle_id("FBS60004")
maruti_swift.set_vehicle_cost(500000)
maruti_swift.set_vehicle_type("Four Wheeler")
maruti_swift.calculate_premium()
maruti_swift.display_vehicle_details()

ktm_duke_490 = Vehicle()
ktm_duke_490.set_vehicle_id("TBS60010")
ktm_duke_490.set_vehicle_cost(500000)
ktm_duke_490.set_vehicle_type("Two Wheeler")
ktm_duke_490.calculate_premium()
ktm_duke_490.display_vehicle_details()