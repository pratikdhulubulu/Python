#  Multileval Inheritance
from os import device_encoding
from re import S
from tkinter import E
from xml.dom.minicompat import defproperty


class Electronics:
    ic = "PIC"
    stock = 8
    def display(self):
        print("class Electronics")
        return f"stoks are {self.stock}"

class Gadget(Electronics):
    vgame = "Py game"
    stock = 9
    def display(self):
        print("class Gadget")
        return f"stoks are {self.stock}"

class phones(Gadget):
    name = "realme"
    stock = 33
    def display(self):
        print("class phones")
        return f"stoks are {self.stock}"

device1 = Electronics()
device2 = phones()

if __name__ == "__main__":
    print(device2.display())