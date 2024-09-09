# Palindrom string
str1 = input("Enter a string : ")
if str1 == str1[::-1]:
    print(f"Entered string '{str1}' is Palindrom")
else:
    print(f"Entered string '{str1}' is Not Palindrom")
