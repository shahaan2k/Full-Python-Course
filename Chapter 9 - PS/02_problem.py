# The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score 

import random # this lines imports the random function in our program


def game():
    print("YOU ARE PLAYING THE GAME")
    score = random.randint (1,100) 
    with open("game.txt") as f: 
        game = f.read() 
        if(game != ""):
            game = int(game)
        else:
            game = 0 

    print(f"YOUR SCORE IS {score}")
    if(score>game):
        with open("game.txt", "w") as f:     
            f.write(str(score)) 
        return score 

game()     
            
               
 