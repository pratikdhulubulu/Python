# Single Inharitance
class Student:
    sub = 5
    def function1(self):
        return self.name, self.std, self.roll, self.sub
    # constructor
    def __init__(self, name, roll, std):
        self.name = name
        self.roll = roll
        self.std = std

class Programmer(Student):
    div = "A"
    def function2(self):
        return self.sub

pd = Student("Pratik", 20, 15)
vb = Student("Vrushabh", 9, 15)
sh = Programmer("Suraj", 33, 15)

if __name__=="__main__":

    print(sh.function1())
    print(sh.function2())
    print(sh.div)
