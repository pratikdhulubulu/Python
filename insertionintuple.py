#insertion in tuple
t1 = (1,4,6,"abc",88)
ele = eval(input("Enter element: "))
list1 = list(t1)
list1.insert(2,ele)
t1 = tuple(list1)
print(t1)