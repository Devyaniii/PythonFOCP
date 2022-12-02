def encrypt():
    x = input("Enter your message: ")
    no_space= x.replace(" ","")
    rev = no_space[::-1]
    print(rev)

encrypt()