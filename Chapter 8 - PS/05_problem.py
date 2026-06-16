# WRITE A FUNCTION FIND THE FACTORIAL OF 'n'

a = int(input("ENTER A NUMBER:"))

def fact(a):
    f = 1
    for i in range(1, a+1):
        f *= i
    print(f"The Factorial Of Given Number is {f}")


fact(a) 
