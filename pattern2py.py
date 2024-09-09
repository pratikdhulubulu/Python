row = int(input("enter no. of rows for pattern : "))
for i in range(1, row + 1):
    print((row-i) * " ",i * "*")
    