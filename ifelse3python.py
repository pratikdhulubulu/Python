sub1 = int(input("enter marks of 1st subject out of 100 : "))
sub2 = int(input("enter marks of 2nd subject out of 100 : "))
sub3 = int(input("enter marks of 3rd subject out of 100 : "))

percentage = (sub1 + sub2 + sub3) / 3
print("percentage obtained : {} %".format(percentage))
if sub1 < 40 or sub2 < 40 or sub3 < 40:
    print("Fail Grade")

elif percentage >= 75:
    print("Outstanding Grade")

elif percentage >= 70 and percentage < 75:
    print("Distinction Grade") 

elif percentage >= 60 and percentage < 70:
    print("A Grade") 

elif percentage >= 50 and percentage < 60:
    print("B Grade")

elif percentage >= 40 and percentage < 50:
    print("C Grade")
    