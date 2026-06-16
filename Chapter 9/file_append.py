# APPEND FUNCTION IN FILE 

st = "THIS TOO SHALL PASS"

f = open("file.txt", "a") # THIS 'a' add another string in our file.txt 
                          
f.write(st)

f.close() 
