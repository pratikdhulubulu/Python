from functools import reduce
from pickle import NONE
from re import X

list1 = ['dustin', 'mike', 'el', 'vill', 'stive', 'robin']
list2 = [2, 3, 4]
# mapedlist = list(map(float,list2))
# print(mapedlist)
newmap = list(map(lambda x : x if x%2==0 else None , list2))
print(newmap)

# def cub(x):
#     return x*x*x 

# def sq(x):
#     return x*x 

# functions = [cub, sq]
# # for i in range(5):
# op = (list(filter(lambda x : x%2==0 ,list2)))
# print(op)

# # redusum = reduce(lambda x, y : x * y , list2)
# # print(redusum)