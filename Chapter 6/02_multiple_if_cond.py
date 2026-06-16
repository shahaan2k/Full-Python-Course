# MULTIPLE IF CONDITIONS 

a = int(input("ENTER YOUR AGE:"))
# If Statement 1:
if(a%2==0):
    print("a is even") # IF STATEMENT IS EXECUTABLE WITHOUT ELSE 

# If Statement 2:
if(a>=18):
    print("YOU'RE ELIGILE FOR DRIVING LICENSE \n YOU CAN APPLY")

elif(a<=0):
    print("YOU'VE ENTERED AN INVALID AGE")

else:
    print("YOU'RE NOT ELIGIBLE FOR DRIVING LICENSE \n WAIT TILL YOU'RE 18" )