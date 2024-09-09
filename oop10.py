# Public Privet Protected
class Electronics:
    ic = "PIC"
    pubstock = 100
    _prostock = 8
    __pristock = 55
    def display(self):
        print("class Electronics")
        return f"stoks are {self.__prostock}"

class Phones(Electronics):
    Gadget = 3
    # def display(self):
    #     print("class Phones")
    #     return f"stoks are {self._prostock}"


opamp1 = Electronics()
opamp2 = Phones()
if __name__ == "__main__":
    print(opamp2.__pristock)
    print(opamp1.display())