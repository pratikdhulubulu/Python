# Palindrom number
num = int(input("enter a number : "))
org_num = num
rev_num = 0

while num > 0:
    digit = num % 10
    num = num // 10
    rev_num = (rev_num * 10) + digit

if rev_num == org_num:
    print(f"{org_num} is a Palindrom number")
else:
    print(f"{org_num} is not a Palindrom number")