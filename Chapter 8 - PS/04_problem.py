# WRITE A FUNCTION TO PRINT THE ELEMENTS OF A LIST IN SAME LINE

countries = ["PAKISTAN", "TURKEY", "ITALY", "SWEEDEN","CANADA"]
cities = ["HUNZA", "SKARDU", "NARAN", "SWAT"] 

def print_el(list):
    for i in list:
        print(i, end=" ")


print_el(cities)

