# Largest number
x = eval(input("enter 1st number : "))
y = eval(input("enter 2nd number: "))

if x == y :
    print("\nboth numbers are same\n")
elif x > y :
    print("{} is largest number".format(x))
else :
    print("{} is largest number".format(y))