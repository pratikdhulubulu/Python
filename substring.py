# Substring
str1 = input("Enter a string : ")
str2 = input("Enter substring : ")
if str2 in str1:
    print(f"'{str2}' is present in '{str1}'")
else:
    print(f"'{str2}' is Not present in '{str1}'")