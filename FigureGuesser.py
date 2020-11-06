print("Hello, this is my FigureGuesser Game. Guess a number maybe you might be lucky.")

import random
import time
time.sleep(3)

num = random.randrange(1, 101)

guess =""

tries= 0
tries_limit = 6

while num != guess and tries != tries_limit:
    guess =int(input("enter a guess: "))
    tries+=1
    
    if guess > num:
        print("too high")
    elif guess < num:
        print("too low")
    elif num == guess and tries == 1:
        print("dang, YOU ARE FUCKING SMART")
    elif num == guess and tries == 2:
        print("whAt a Genius")
    elif num == guess and tries == 3:
        print("nice try!!")
    elif num == guess and tries== 4:
        print("nice try!! ")
    elif num == guess and tries == 5:
        print("dumb ass, THAT WAS CLOSE")
        
if tries == tries_limit :
    print("YOU LOSE!!! MOTHERFUCKER")
    
print("number of tries: ", tries)