class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return "{}.{}@mail.com".format(self.first, self.last)
        #allows one to change the value of the email function and 
        # call the function without brackets ()
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        # enabled me to change,set and 'save' the first and last names
    
    @fullname.deleter
    def fullname(self):
        print("deleted name!")
        self.first = None
        self.last = None
        # deleted the fullname attribute

emp_1 = Employee("Keren", "Mungai")
emp_1.first = "Jane"
emp_1.fullname = "Jane Musyoka"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname