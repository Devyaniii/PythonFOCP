BAD_PASSWORD = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while (True):
    pa = str(input("Enter your pass: "))
    num = len(pa)
    if pa in BAD_PASSWORD:
        print("Try entering a different password!")
        continue
    else:
        if num > 8 and num <= 12:
            print("password set")   
            break
        else:
            print("password must be between 8 and 12 characters! ")
            continue