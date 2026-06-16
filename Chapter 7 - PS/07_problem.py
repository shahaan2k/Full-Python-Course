# WRITE A PROGRAM TO PRINT A STAR PATTERN 

n = int(input("Enter A Number:"))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"*(2*i-1))
    # print("")

