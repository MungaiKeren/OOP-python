class Students:

    num_of_students = 0

    def __init__(self, admn, fname, lname):
        self.admn = admn
        self.fname = fname
        self.lname = lname

        Students.num_of_students += 1
    
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

std_2 = Students(2,"Eunice","Wanjiru")

class Parents(Students):

    num_of_parents = 0

    def __init__(self,admn,fname,lname,stdname=None):
        super().__init__(admn,fname,lname)
        if stdname is not None:
            self.stdname = stdname
        else:
            self.stdname = []

        Parents.num_of_parents +=1
    
    def add_std(self, std):
        if std not in self.stdname:
            self.stdname.append(std)
    
    def print_parentStudent(self):
        for std in self.stdname:
            print("****", std.fullname())

std_1 = Students(1,"Mark","Mungai")
prnt_1 = Parents(3,"Johnson","Mungai",[std_1])

print(prnt_1.print_parentStudent())