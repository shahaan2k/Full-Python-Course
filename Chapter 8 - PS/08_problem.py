# RECURSION 
# WRITE A PROGRAM FOR BACKWARD COUNTING 

# RECURSIVE FUNCTION 

def count(n):
    if(n == 0):
        return 
    
    print(n)
    count(n-1)

count(6)        