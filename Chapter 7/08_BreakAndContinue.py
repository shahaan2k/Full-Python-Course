# Break And Continue Statement

# Break Statement
for i in range(100):
    if(i==50): # Loop Will Execute From 0 To 49 Times 
        break # Break Statement Terminates A Loop When Our Loop Reaches The If Condition
    print(i) 

# Continue Statement
for i in range(100):
    if(i==50): # When Loop Reaches 50th Iteration It Will Skip 50 
        continue # Continue Statement Skips The Desired Iteration In Our If Condition
    print(i)

# Pass Statement
for i in range(10):
    pass

i = 0
while(i<45):
    print(i)
    i =+1 