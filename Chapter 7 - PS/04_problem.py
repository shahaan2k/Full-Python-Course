# Write a program to find whether a given number is prime or not

n = int(input("Enter A Number:"))

for i in range(2, n):
    if(n%2) == 0:
        print("Not A Prime Number")
        break
else:
    print("A Prime Number")        