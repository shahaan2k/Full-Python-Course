# WRITE A PROGRAM TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER USING FOR LOOP
num = int(input("Enter A Number:"))
product = 1
numRange = range(1 , num+1)
# print(numRange)
for i in numRange:

    product = product * i
    print(product)
print(f"THE FACTORIAL OF {num} IS {product}")  

