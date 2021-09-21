class Employee:

    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@mail.com"
        self.pay = pay
        Employee.num_of_emp += 1
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Lilian", "Muli", 80000)
emp_2 = Employee("Waihiga", "Mwaura", 80000)
emp_3 = Employee("Yvonne", "Okwara", 80000)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("Mark", "Kabutha", 10000, "Java")
dev_2 = Developer("Christine", "SHiku", 10000, "Python")

class Manager(Employee):
    def __init__(self, first, last, pay, assignees = None):
        super().__init__(first, last, pay)
        if assignees is not None:
            self.assignees = assignees
        else:
            self.assignees = []
    
mngr_1 = Manager("Mary", "Wambui", 300000, [dev_1])

