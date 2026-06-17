# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

word = "donkey"
 
with open("word.txt") as f:
    content = f.read()  
    
content = content.replace(word, "####")

with open("word.txt", "w") as f:
    f.write(content)

