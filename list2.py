import itertools
x = [1,2,3,5,1,7]
t = 6
result = [res for i in range (len(x),0,-1)
 for res in itertools.combinations(x,i) if sum(res)==t]
print(result)