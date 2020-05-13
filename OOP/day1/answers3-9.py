#OOPR-Assgn-3
#Start writing your code here
class Customer:
    def __init__(self):
        self.customer_name=None
        self.bill_amount=None
    
    def purchases(self):
        discounted_amount=self.bill_amount-self.bill_amount*0.05
        self.pays_bill(discounted_amount)
        
    
    def pays_bill(self,amount):
        print(self.customer_name," pays bill amount of Rs",amount)
    
        
sandra=Customer()
sandra.customer_name="Sandra"
sandra.bill_amount=1000
sandra.purchases()
john=Customer()
john.customer_name="John"
john.bill_amount=500
john.purchases()
# from GOPIKA to All Participants:

#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def set_name(self, name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

#OOPR-Assgn-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            
# from GOPIKA to All Participants:
#OOPR-Assgn-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            
# from GOPIKA to All Participants:
def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount=self.__vehicle_cost*(2/100)
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount=self.__vehicle_cost*(6/100)
        else:
            print("Invalid input")
            print("Invalid vehicle type")
            
    def display_vehicle_details(self):
        print(self.__vehicle_id," / ", self.__vehicle_type," / ", self.__vehicle_cost," / ", self.__premium_amount)
v1=Vehicle()
v1.set_vehicle_id("KA-09-HD-7555")
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(50000)
v1.calculate_premium()
v1.display_vehicle_details()
# from GOPIKA to All Participants:
#OOPR-Assgn-7
#Start writing your code here
class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__technology_skill=None
        self.__avg_feedback=None
        self.__experience=None
        
    def set_instructor_name(self,instructor_name):
        self.__instructor_name = instructor_name
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
        
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
        
    def set_experience(self,experience):
        self.__experience=experience 
    def get_instructor_name(self):
        return self.__instructor_name
    def get_technology_skill(self):
        return self.__technology_skill
    def get_avg_feedback(self):
        return self.__avg_feedback
    def get_experience(self):
        return self.__experience        
        
    def allocate_course(self,technology):
        counter=0
        if(self.check_eligibility()):
            for tech in self.__technology_skill:
                if(tech==technology):
                    counter+=1    
            if(counter>=1):   
                return True
            else:
                return False
        else:
            return False
    
def check_eligibility(self):
        if(self.__experience>3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False  
        
instructor1=Instructor()
instructor1.set_instructor_name("Jack")
instructor1.set_technology_skill(["JAVA","C++"])
instructor1.set_avg_feedback(5)
instructor1.set_experience(5)
if(instructor1.allocate_course("JAVA")==True):
    print("Instructor successfully allocated")
else:
    print("Instructor is not allocated")



 #OOPR-Assgn-8
#Start writing your code here
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    
    def set_student_id(self,student_id):
        self.__student_id=student_id
        
    def set_marks(self,marks):
        self.__marks=marks
        
    def set_age(self,age):
        self.__age=age 
        
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age()  and self.__marks>=65):
            return True
        else:
            return False
        
    def validate_marks(self):
        if(self.__marks>=0 and self.__marks<=100 ):
            return True
        else:
            return False
            
    def validate_age(self):
        if(self.__age>20):
            return True
        else:
            return False
student=Student() 
student.set_student_id(1004)
student.set_age(21)
student.set_marks(65)
if(not student.validate_marks() and not student.validate_age()):
    print("Invalid qualifying exam marks")
    print("Invalid age")
elif(not student.validate_marks()):
    print("Invalid qualifying exam marks")
elif(not student.validate_age()):
    print("Invalid age")
elif(student.check_qualification()):
    print("Eligible for admission")
else:
    print("Not eligible for admission")




    #OOPR-Assgn-9
#Implement Student class here
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None
        
    def set_student_id(self,student_id):
        self.__student_id=student_id
        
    def set_marks(self,marks):
        self.__marks=marks
        
    def set_age(self,age):
        self.__age=age 
        
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
    
    def validate_marks(self):
        if(self.__marks>=0 and self.__marks<=100):
            return True
        else:
            return False
        
    def validate_age(self):
        if(self.__age>20):
            return True