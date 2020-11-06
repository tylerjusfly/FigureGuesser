print("Hello, this is my FigureGuesser Game. Guess a number maybe you might be lucky.")

#importing random. random guess any figure and prints it out

import random
#importing time and delaying it for 3sec
import time
time.sleep(3)

#passing random to var and giving it a minimum and maximum guessing number
num = random.randrange(1, 101)

guess =""

tries= 0
tries_limit = 6

while num != guess and tries != tries_limit:
    guess =int(input("enter a guess: "))
    tries+=1
 #putting the optionals statements into practice   
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
