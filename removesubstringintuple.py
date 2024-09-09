#remove substring in tuple
t1 = (1,4,"pd",5.33,"abc",4,"pd")
sub = input("enter substring : ")
for i in t1:
    if i == sub:
        j = t1.index(sub)
        t1 = (t1[:j] + t1[j+1:])
print(t1)