class Monkey:
    def __init__(self,color,breed,cycle):
        self.color=color
        self.breed=breed
        self.cycle=cycle
class Cycle:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
c1=Cycle("Blue","Ladybird")
m1=Monkey("Black","Gorilla",c1)
print(m1.color,m1.cycle.brand)
from Ashok Kumar Sivanantham to All Participants:
class Monkey:
    def __init__(self,color,breed,cycle):
        self.color=color
        self.breed=breed
        self.cycle=cycle
class Cycle:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
c1=Cycle("Blue","Ladybird")
m1=Monkey("Black","Gorilla",c1)
print(m1.color,m1.cycle.brand)


# from Ashok Kumar Sivanantham to All Participants:
class Monkey:
    def __init__(self,color,breed,cycle):
        self.color=color
        self.breed=breed
        self.cycle=cycle
    def eat(self):
        print("Monkey is eating...")
        
class Cycle:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    def cycling(self):
        return "Cycle riding..."
c1=Cycle("Blue","Ladybird")
m1=Monkey("Black","Gorilla",c1)
c2=Cycle("Red","Hercules")
m2=Monkey("Brown","Chimpu",c2)
print(m1.color,m1.breed,m1.cycle.color,m1.cycle.brand,m1.cycle.cycling())
print(m2.color,m2.breed,m2.cycle.color,m2.cycle.brand,m2.cycle.cycling())


# from Ashok Kumar Sivanantham to All Participants:
class Monkey:
    def __init__(self,color,breed,cycle):
        self.__color=color
        self.__breed=breed
        self.cycle=cycle
    def set_color(self,color):
        self.__color=color
    def set_breed(self,breed):
        self.__breed=breed
    def get_color(self):
        return self.__color
    def get_breed(self):
        return self.__breed
    def eat(self):
        print("Monkey is eating...")
        
class Cycle:
    def __init__(self,color,brand):
        self.__color=color
        self.__brand=brand
    def set_color(self,color):
        self.__color=color
    def set_brand(self,brand):
        self.__brand=brand
    def get_color(self):
        return self.__color
    def get_brand(self):
        return self.__brand
    def cycling(self):
        return "Cycle riding..."
c1=Cycle("Blue","Ladybird")
m1=Monkey("Black","Gorilla",c1)
c2=Cycle("Red","Hercules")
m2=Monkey("Brown","Chimpu",c2)
print(m1.get_color(),m1.get_breed(),m1.cycl


# from Ashok Kumar Sivanantham to All Participants:
class Monkey:
    def __init__(self,color,breed,cycle):
        self.__color=color
        self.__breed=breed
        self.cycle=cycle
    def set_color(self,color):
        self.__color=color
    def set_breed(self,breed):
        self.__breed=breed
    def get_color(self):
        return self.__color
    def get_breed(self):
        return self.__breed
    def eat(self):
        print("Monkey is eating...")
        
class Cycle:
    def __init__(self,color,brand):
        self.__color=color
        self.__brand=brand
    def set_color(self,color):
        self.__color=color
    def set_brand(self,brand):
        self.__brand=brand
    def get_color(self):
        return self.__color
    def get_brand(self):
        return self.__brand
    def cycling(self):
        return "Cycle riding..."
c1=Cycle("Blue","Ladybird")
m1=Monkey("Black","Gorilla",c1)
c2=Cycle("Red","Hercules")
m2=Monkey("Brown","Chimpu",c2)
print(m1.get_color(),m1.get_breed(),m1.cycl