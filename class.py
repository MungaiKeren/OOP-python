# Python OOP

class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # this variable here is a class variable

    def __init__(self, first, last, pay): # self makes the method here an instance of the class
        # first, last and pay are other arguments that could be passed on to the method
        self.first = first
        self.last = last
        self.email = first + "." + last + "@mail.com"
        self.pay = pay

        Employee.num_of_emps += 1
    
    def fullname(self):
        # return self.first + " "+ self.last
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Keren", "wambui", 50000)
emp_2 = Employee("Chris", "Mwangi", 60000)
Employee.set_raise_amount(1.06)

import datetime as dt
my_day = dt.date(2020,5,27)

check_date = Employee.is_weekday(my_day)

# creating a subclass of the class Employee
class Developer(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, prog_lang): #subclassing
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("----->",emp.fullname())


dev_1 = Developer("Chris", "Martin", 300000,"Python")
# developer class inherits all attributes of the Employee class
dev_2 = Developer("Britney", "Hilton", 200000,"R")

mgr_1 = Manager("John", "Kim", 500000, [dev_1])

print(mgr_1.print_emps())

