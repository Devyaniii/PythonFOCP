def int_fac():
    num = int(input("Enter a number: "))
    factorial=1
    if num>0:
        for x in range(1,num + 1):
            factorial = factorial*x
        print(f"The factorial of {num} is {factorial}")
    else:
        print("Invalid")

int_fac()