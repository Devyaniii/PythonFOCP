nu = int(input("Enters the number of the table you require: "))
if nu > 0:
    for nu1 in range(0,11):
        mul = nu1 * nu
        print(nu1,"*",nu ,"=", mul)
else:
    nu2 = -nu
    for nu1 in range(10,-1,-1):
        mul = nu1 * nu2
        print(nu1,"*",nu2 ,"=", mul)