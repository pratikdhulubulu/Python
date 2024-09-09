str1 = input("Enter a string : ")
if len(str1) >= 3:
    if str1.endswith("ing"):
        print(str1 + "ly")
    else:
        print(str1 + "ing")  
else:
    print("Error 404 Rushabh Bastwad Access Denied...!!!")          