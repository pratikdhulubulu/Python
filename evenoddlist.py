#even odd list
list1 = [1,2,17,5,6,7,89,32,565,90]
even = list()
odd = list()
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)            