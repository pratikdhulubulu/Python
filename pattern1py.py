import time
row = int(input("enter no. of rows for pattern : "))
for i in range(1, row + 1):
    print(i * "*",end = " ")
    time.sleep(2)
    print()
time_now = time.asctime(time.localtime(time.time()))    
print(time_now)    