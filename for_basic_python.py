# display natural numbers from 11 to 25
print("natural numbers from 11 to 25 are :")
for num in range(11,26):
    print(num,end=" ")

# print numbers from 1 to 50 which are divisible by 5
print("\nnumbers from 1 to 50 which are divisible by 5 are :")
for num in range(5,51,5):
    print(num,end=" ")

print()

# or
print("numbers from 1 to 50 which are divisible by 5 are :")
print(list(range(5,51,5)))

# count of numbers which are divisible by 2 from 0 to 50
print("count of numbers which are divisible by 2 from 0 to 50 is :")
print(len(list(range(2,51,2))))