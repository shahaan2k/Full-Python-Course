# Write a program to calculate the grade of a student from his marks
#  from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter Your Marks:"))

if(marks>90):
    print("Your Grade: EX")

elif(marks>80 or marks ==90):
    print("Your Grade: A")

elif(marks>70 or marks ==80):
    print("Your Grade: B")

elif(marks>60 or marks ==70):
    print("Your Grade: C")

elif(marks>=50 or marks ==60):
    print("Your Grade: D")

elif(marks<50):
    print("Your Grade: F")        