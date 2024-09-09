# f = open("fileh.txt","r+")
# print(f.readline(),end="")
# print(f.readline())
# print(f.readlines())
# f.write("\nsiya siya")
# f.close()
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

sum = lambda num1,num2 : num1+num2
print(sum(num1,num2))