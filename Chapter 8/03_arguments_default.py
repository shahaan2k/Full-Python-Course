# DEFAULT ARGUMENTS

def greet(name, ending="Thank You"): # Here We Have Stored The Default
    print("Have A Good Day,", name)  # Value  Of 'Ending' Variable As
    print(ending)                                 # 'Thank You'  
greet("SHAHAAN") # Its Printing Thank You As An Output For 'ending'
                 # Because We Havent Defined It In The Function Call
# For Example

def greet(name, ending="Thank You"):
    print("Have A Good Day,", name)   
    print(ending)
greet("SHAHAAN")
greet("Dayyan","Thanks") # As You Can See Here I Have Defined The Value
                         # Of 'ending' Variable As "Thanks" If I Didn't 
                         # Defined It The Output Would Be "Thank You" As 
                         # Default Value  


                