class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__experience = None
        self.__avg_feedback= None
        self.__technology_skill = None

    def get_instructor_name(self):
        return self.__instructor_name
    def set_instructor_name(self,instructor_name):
        self.__instructor_name = instructor_name
    
    def get_experience(self):
        return self.__experience
    def set_experience(self,experience):
        self.__experience = experience
    
    def get_avg_feedback(self):
        return self.__avg_feedback
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback = avg_feedback
    
    def get_technology_skill(self):
        return self.__technology_skill
    def set_technology_skill(self,technology_skill):
        self.__technology_skill = technology_skill

    def check_eligibility(self):
        if(self.__experience>3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False
    
    def allocate_course(self, technology):
        skill_count = 0
        if self.check_eligibility():
            for skill in self.__technology_skill:
                if skill in technology:
                    skill_count += 1
            if skill_count > 0:
                return True
            else:
                return False
        else:
            return False


instructor1 = Instructor()
instructor1.set_instructor_name("Maya")
instructor1.set_experience(5)
instructor1.set_avg_feedback(4.7)
instructor1.set_technology_skill(["DBMS", "Java"])

instructor1.allocate_course("DBMS")

# print(instructor1.get_technology_skill())
if instructor1.allocate_course("DBMS"):
    print("Course Allotted")
else:
    print("Course not Allotted")