# Multiple Inheritance
from mimetypes import init
from re import S

class Student:
    sub = 9
    def __init__(self, name, prn):
        self.name = name
        self.prn = prn
    def display(self):
        print("class Student")
        return f"Name is {self.name} PRN is {self.prn} and subjects are {self.sub}"

class Programmer:
    sub = 5
    def __init__(self, name, prn):
        self.name = name
        self.prn = prn
    def display(self):
        print("class Programmer")
        return f"Name is {self.name} PRN is {self.prn} and subjects are {self.sub}"

class Player(Student, Programmer):
    print("class pl")
    def __init__(self, name, prn):
        self.name = name
        self.prn = prn
    def display(self):
        print("class Player")
        return f"Name is {self.name} PRN is {self.prn} and subjects are {self.sub}"


pd = Player("pratik", 20)
vb = Programmer("vrushabh", 9)
sh = Player("suraj", 33)

if __name__== "__main__":
    print(pd.sub)
    print(pd.display())

