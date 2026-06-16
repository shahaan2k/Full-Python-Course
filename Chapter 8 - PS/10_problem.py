# WRITE A RECURSIVE FUNCTION TO PRINT SUM OF N NATURAL NUMBERS 

n = int(input("ENTER THE NUMBER :"))

def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n-1)+ n

result = sum(n)
print(result) 