# SNAKE WATER GUN GAME PROJECT

import random 

computer = random.choice([-1, 0, 1]) 

option = input("ENTER THE FIRST LETTER OF YOUR CHOICE i.e(S,W,G):") 
optionDict = {"s" : 1, "w" : -1, "g" : 0 } 
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"} 

user = optionDict[option]  # HERE WE HAVE STORED THE VALUE OF THE USER IN USER VARIABLE

print(f"YOU CHOSE {reverseDict[user]}\nCOMPUTER CHOSE {reverseDict[computer]}")

if(computer==user):
    print("ITS A DARW")
else:
    if(computer== -1 and user== 1):
        print("CONGRATULATIONS, YOU WIN")

    elif(computer== -1 and user== 0):
        print("Sorry, YOU LOSE")

    elif(computer== 1 and user== -1):
        print("Sorry, YOU LOSE") 

    elif(computer== 1 and user== 0):
        print("CONGRATULATIONS, YOU WON")

    elif(computer== 0 and user== 1):
        print("SORRY, YOU LOSE")    

    elif(computer== 0 and user== -1):
        print("CONGRATULATIONS, YOU WON")
    else:
        print("SOMETHING WENT WRONG")     
               