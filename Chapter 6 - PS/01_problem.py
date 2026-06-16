# WRITE A PROGRAM THAT TAKES 4 NUMBERS FROM THE USER AND PRINTS GREATER NUM

a1 = int(input("ENTER NUMER 1:"))
a2 = int(input("ENTER NUMER 2:"))
a3 = int(input("ENTER NUMER 3:"))
a4 = int(input("ENTER NUMER 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1) 

elif(a2>a1 and a2>a3 and a2>a4):
    print(a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print(a3)    

else:
    print(a4)
                    