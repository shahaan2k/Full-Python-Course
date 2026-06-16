# WRITE A PROGRAM TO READ A TEXT FROMA GIVEN FILE POEMS.TXT AND FIND OUT
# WHEATHER IT CONTAINS TWINKLE OR NOT 

f = open("poems.txt") 
content = f.read()
if("twinkle" in content):
    print("YES TWINKLE IS PRESENT")
else:
    print("NO ITS NOT PRESENT ") 

f.close()