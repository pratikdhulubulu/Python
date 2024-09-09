#count str in list
list1 = ["aba",8,"aaa","ass",3,"55","k","jj",7]
count = 0
for i in list1:
    if type(i) == str and len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(count)