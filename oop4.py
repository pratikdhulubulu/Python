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

    # @classmethod
    # def split(cls, string):
    #     sp = string.split(".")
    #     return cls(sp[0], sp[1], sp[2])

    @classmethod
    def split(cls, string):
        return cls(*string.split("."))
          
pd = Student("Pratik", 20, 15)
vb = Student.split("Vrushabh.9.15")

if __name__=="__main__":
    print(vb.function1())
