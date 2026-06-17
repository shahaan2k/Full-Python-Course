# Repeat program 4 for a list of such words to be censored.

words = ["stupid", "animals", "idiot", "idiotic"]

with open("list.txt") as f:
    content = f.read()  
    for word in words:
        content = content.replace(word, "####")

with open("list.txt", "w") as f:
    f.write(content)