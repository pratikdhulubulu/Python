j=0
l = [1,2,3,5,1,7]
sum = 0
i = 0
l2=[]

for i in range (0,len(l)):
    sum=sum+l[i]
    if sum>6:
        while j<i:
            if sum>6:
                sum=sum-l[j]
                j =j+1                            
    elif sum==6:
        #print(l[j:i+1])
        l2.append(l[j:i+1])

print(l2)               
