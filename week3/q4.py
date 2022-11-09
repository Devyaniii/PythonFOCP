BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
pa= input("enter your password:")
pa1 = input("enter your password again:")
if 8<=len(pa)<=12 and pa==pa1:
    if pa not in BAD_PASSWORDS and pa1 not in BAD_PASSWORDS:
        print("password set")
    else:
        print("bad password")
else:
    print("ERROR!!!")