class Employee:
    def __init__(self,name, age, salary):
        self.emp_id = name
        self.emp_name = age
        self.emp_salary = salary

    def display(self):
        print(str(self.emp_name),str(self.emp_id) + " earns " + str(self.emp_salary))


jack = Employee("Jack", 24, 30000)
jack.display()
jill = Employee("Jill", 27, 40000)
jill.display()