class Student:
    sub = 5
    def function1(self):
        return self.sub ,self.name, self.std, self.roll
    # constructor
    def __init__(self, roll, std):
        self.roll = roll
        self.std = std
        


pd = Student(20, 15)
vb = Student(9, 15)

pd.name = "Pratik"
vb.name = "Vrushabh"
if __name__=="__main__":
    print(pd.function1())