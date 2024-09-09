def fun(f):
    print("I am happy...!")
    f()
    print("I am very happy.....!")


@fun
def fun1():
    print("pratik")

@fun
def fun2():
    print(2*8)