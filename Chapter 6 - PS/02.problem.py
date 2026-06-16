# WRITE A PROGRAM THAT TAKES THE MARKS OF 3 SUBJECTS FROM A STUDENT &
# FINDS THE PERCENTAGE AND TELLS WHEATHER HE/SHE IS PASS OR FAIL
# SUBJECT PASSING MARKS ARE 33 MINIMUM 

marks1 = int(input("ENTER SUBJ 1 MARKS:"))
marks2 = int(input("ENTER SUBJ 2 MARKS:"))
marks3 = int(input("ENTER SUBJ 3 MARKS:"))

total_percentage = (marks1 + marks2 + marks3)/300*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("YOU'RE PASS, CONGRATULATION", total_percentage)
else:
    print("""YOU FAILED BUT REMEMBER A MAN IS NOT GREAT BECAUSE HE HASN'T FAILED,
           A MAN IS GREAT BECAUSE FAILURE HASN'T STOPPED HIM""")    