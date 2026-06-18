# Create a student grade management program 

per = int(input("ENTER YOUR PERCENTAGE FOR GRADE INFORMATION:"))

if(per>=90 and per<=100):
    print("YOUR GRADE IS A+")

elif(per>=80 and per<=90):
    print("YOUR GRADE IS A")

elif(per>=70 and per<=80):
    print("YOUR GRADE IS B")

elif(per>=60 and per<=70):
    print("YOUR GRADE IS C")

elif(per>=50 and per<=60):
    print("YOUR GRADE IS D")

elif(per>=40 and per<=50):
    print("YOUR GRADE IS E")

else:
    print("SORRY, YOU'RE FAIL TRY AGAIN NEXT YEAR :)")
