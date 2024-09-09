class Student:
    sub = 5
    def function1(self):
        return self.name, self.std, self.roll, self.sub
    # constructor
    def __init__(self, name, roll, std):
        self.name = name
        self.roll = roll
        self.std = std

    @staticmethod
    def simplefun(num):
        print("I am a simple function",num)


pd = Student("Pratik", 20, 15)
vb = Student("Vrushabh", 9, 15)

if __name__=="__main__":
    
    print(vb.function1())
    Student.simplefun(14)
