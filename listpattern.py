#list pattern
list1 = ["p","q"]
new = list()
n = int(input("Enter num n : "))
for i in range(1,n+1):
    for j in list1:
        new.append(f"{j}{i}")
print(new)        