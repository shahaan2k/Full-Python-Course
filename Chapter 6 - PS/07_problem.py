# Write a program to find out whether a given post is talking about
# “Harry” or not

post = input("Enter your Post: ")

if("harry" in post.lower()):
    print("Harry Is Mentioned In The Post")
else:
    print("Harry Is Not Mentioned In The Post")

