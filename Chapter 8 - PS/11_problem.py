# WRITE A RECURSIVE FUNCTION TO PRINT ALL THE ELEMENTS IN LIST

rooms = [1, 2, 3, 4, 5, 6, 7, 8,]

def elem(list, idx=0):
    if(idx == len(list)):
        return 
    else:
        print(list[idx])
        elem(list, idx+1)

elem(rooms)