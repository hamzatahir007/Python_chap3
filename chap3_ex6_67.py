#guessing number modifying

guess= 1

import random
winning_number = random.randint(1 , 100)
guessing_number = int(input("Guess a number from 0 to 100 :"))
game_over= False


while not game_over:
    if winning_number == guessing_number:
        print(f"YOU WIN , and you try this number in {guess} times")
        game_over=True

    else :
        if  winning_number > guessing_number:
             print("Too Low")
             guess = guess + 1
             guessing_number = int(input("Guess again: "))
        else:
             print("Too high")
             guess = guess + 1
             guessing_number = int(input("Guess again: "))
