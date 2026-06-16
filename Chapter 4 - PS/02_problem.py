# WRITE A PROGRAM THAT ACCEPTS THE MARKS OF 6 STUDENTS AND DISPLAY THEM IN SORTED MANNER 

marks = []

m1 = int(input("Marks Of Roll No 1:"))
marks.append(m1)
m2 = int(input("Marks Of Roll No 2:"))
marks.append(m2)
m3 = int(input("Marks Of Roll No 3:"))
marks.append(m3)
m4 = int(input("Marks Of Roll No 4:"))
marks.append(m4)
m5 = int(input("Marks Of Roll No 5:"))
marks.append(m5)
m6 = int(input("Marks Of Roll No 6:"))
marks.append(m6)

marks.sort()
print(marks)
