# FUNCTIONS WITH ARGUMENTS

def greet():
    print("Have A Good Day")

greet() # THIS IS A SIMPLE FUNCTION WITH ARGUMENT 

# HERE IS A BIT COMPLICATED ONE 

def greet(name): # WE CAN ALSO STORE VARIABLES IN IT
    print("Have A Good Day,", name)

greet("SHAHAAN") 

# return Value 

def greet(name): # WE CAN ALSO STORE VARIABLES IN IT
    print("Have A Good Day,", name)
    return "OK"

a = greet("Have A Good Day," "SHAHAAN")

print(a)


