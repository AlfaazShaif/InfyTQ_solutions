#OOPR-Assgn-10
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type
        
class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            a=i.split(',')
            b=CallDetail(a[0],a[1],a[2],a[3])
            self.list_of_call_objects.append(b)
            
            
    
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)



#OOPR-Assgn-11
#Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available
    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
    def validate_flower(self):
        if self.__flower_name.upper()=="ORCHID" or self.get_flower_name().upper()=="ROSE" or self.get_flower_name().upper()=="JASMINE":
            return True
        return False 
    
    def validate_stock(self,required_quantity):
        if required_quantity<=self.get_stock_available():
            return True
        return False
    
    def sell_flower(self,required_quantity):
        if self.validate_flower()==True and self.validate_stock(required_quantity)==True:
           
            self.set_stock_available(self.get_stock_available()-required_quantity)
    
    def check_level(self):
        if self.get_flower_name().upper()=="ORCHID" and self.get_stock_available()<15:
            return True
        elif self.get_flower_name().upper()=="ROSE" and self.get_stock_available()<25:
            return True
        elif self.get_flower_name().upper()=="JASMINE" and self.get_stock_available()<40:
            return True
        return False
    
    
flower1=Flower()
flower1.set_flower_name("Rose")
flower1.set_price_per_kg(50)
flower1.set_stock_available(20)
print(flower1.sell_flower(15))
print(flower1.check_level())



#OOPR-Assgn-12
#Start writing your code here
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None
    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        
        self.__bill_amount=0.0
        for i in range(0,len(quantity_list)):
            self.__bill_amount=self.__bill_amount+quantity_list[i]*price_list[i]
        self.__bill_amount=self.__bill_amount+consultation_fees
bill1=Bill(101, "Prachi")
quantity_list=[2,1,6,3]
price_list=[100,150,50,60]
bill1.calculate_bill_amount(500, quantity_list, price_list)
print("Bill id:",bill1.get_bill_id())
print("Patient name:",bill1.get_patient_name())
print("Bill amount:",bill1.get_b


# from GOPIKA to All Participants:
#OOPR-Exer-6
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.mileage=None
        self.fuel_left=None
    
    def identify_distance_that_can_be_travelled(self):
        fuel_quantity=self.fuel_left
        max_distance=0
        while(fuel_quantity>5):
            max_distance=max_distance+self.mileage
            fuel_quantity-=1
        return max_distance
    
    def identify_distance_travelled(self, initial_fuel):
        fuel_used=initial_fuel-self.fuel_left
        distance_travelled=fuel_used*self.mileage
        return distance_travelled
    
        
car=Vehicle()
car.mileage=12
car.fuel_left=12
print("Maximum distance that can be travelled: ",car.identify_distance_that_can_be_travelled())
print("Distance travelled:",car.identify_distance_travelled(20))


#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list=["L101","L102","L103","L104"]
    @staticmethod
    def search_classroom(class_room):
        if class_room.upper() in Classroom.classroom_list:
            return "Found"
        return -1
print(Classroom.search_classroom("L103"))

# 
# 
class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects=None
    def parse_customer(self,list_of_customers,list_of_calls):
        self.list_of_customer_calldetail_objects=[]
        for i in range(0,len(list_of_customers)):
            new_l=[]
            for j in range(0,len(list_of_calls)):
                if(list_of_customers[i].phone_no==list_of_calls[j].phone_no):
                    new_l.append(list_of_calls[j])
            list_of_customers[i].list_of_calls=new_l
            self.list_of_customer_calldetail_objects.append(list_of_customers[i])