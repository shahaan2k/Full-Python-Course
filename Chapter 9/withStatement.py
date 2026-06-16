# WITH STATEMENT 

# NORMAL WAY OF OPENING A FILE 
# f = open("file.txt")
# data = f.read()
# print(data)

# f.close()  

# ANOTHER WAY OF OPENING A FILE WITHOUT CLOSE() 
with open("file.txt") as f:
    print(f.read()) 