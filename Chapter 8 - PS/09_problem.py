# WRITE A RECURSIVE FUNCTION TO FIND THE FACTORIAL OF A NUMBER 'n'

n = int(input("ENTER A NUMBER :"))

def fact(n):
    if(n == 0 or n == 1):
        return 1 
    else:
        return n * fact(n-1)
        
result = fact(n)    
print(f"THE FACTORIAL OF GIVEN NUMBER IS : {fact(n)}") 