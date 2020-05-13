class Mobile:
    __counter=0
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount=50
        Mobile.__counter+=1
    @staticmethod
    def get_counter(): 
        return Mobile.__counter 
  
    def purchase(self):
        
        print(Mobile.discount)
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
print(Mobile.get_counter())
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
class Mobile:
    __counter=0
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount=50
        Mobile.__counter+=1
    @staticmethod
    def get_counter(): 
        return Mobile.__counter 
  
    def purchase(self):
        
        print(Mobile.discount)
        total = self.price - self.pr




# class Mobile:
#     __counter=0
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#         self.discount=50
#         Mobile.__counter+=1
#     @staticmethod
#     def get_counter(): 
#         return Mobile.__counter 
  
#     def purchase(self):
        
#         print(Mobile.discount)
#         total = self.price - self.price * self.discount / 100
#         print (self.brand, "mobile with price", self.price, "is available after discount at", total)
# print(Mobile.get_counter())
# mob1=Mobile(20000, "Apple")
# mob2=Mobile(30000, "Apple")
# mob3=Mobile(5000, "Samsung")
# class Mobile:
#     __counter=0
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#         self.discount=50
#         Mobile.__counter+=1
#     @staticmethod
#     def get_counter(): 
#         return Mobile.__counter 
  
#     def purchase(self):
        
#         print(Mobile.discount)
#         total = self.price - self.pr


# class Mobile:
#     __counter=0
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#         self.discount=50
#         Mobile.__counter+=1
#     @staticmethod
#     def get_counter(): 
#         return Mobile.__counter 
  
#     def purchase(self):
        
#         print(Mobile.discount)
#         total = self.price - self.price * self.discount / 100
#         print (self.brand, "mobile with price", self.price, "is available after discount at", total)
# print(Mobile.get_counter())
# mob1=Mobile(20000, "Apple")
# mob2=Mobile(30000, "Apple")
# mob3=Mobile(5000, "Samsung")
# class Mobile:
#     __counter=0
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#         self.discount=50
#         Mobile.__counter+=1
#     @staticmethod
#     def get_counter(): 
#         return Mobile.__counter 
  
#     def purchase(self):
        
#         print(Mobile.discount)
#         total = self.price - self.pr