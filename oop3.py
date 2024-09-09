class Student:
    sub = 5
    def function1(self):
        return self.name, self.std, self.roll, self.sub
        
    # constructor
    def __init__(self, name, roll, std):
        self.name = name
        self.roll = roll
        self.std = std

    @classmethod
    def modifysub(cls, newsub):
        cls.sub = newsub 

pd = Student("Pratik", 20, 15)
vb = Student("Vrushabh", 9, 15)

if __name__=="__main__":
    pd.modifysub(9)
    print(Student.sub)
    print(vb.sub)
