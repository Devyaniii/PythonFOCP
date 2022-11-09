pa= input("enter your password:")
pa1 = input("enter your password again:")
if 8<=len(pa)<=12 and pa==pa1:
    print("password set")
else:
    print("ERROR!!!")
