import mailcap
from unicodedata import name


def fun1(narg, *parg, **dparg):
    for i in parg:
        print(narg * i)

def makeastr(string):
    print(f"This is my string {string} ")
    
     
mult = 2
list1 = [2, 3, 4, 5, 6]

if __name__ =='__main__':

    fun1(mult, *list1)
