# Prime number
num = int(input("enter a number : "))
flag = 0
for div in range(2, num):
    if num % div == 0:
        print(f"{num} is not a prime number")
        flag = 1
        break
if flag == 0:
    print(f"{num} is a prime number")    