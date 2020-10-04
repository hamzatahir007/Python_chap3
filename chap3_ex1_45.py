#exercise chap3 number guessing game

winning_number = 57
guess_number = int(input("Guess any numbers from 1 to 100: "))

if winning_number == guess_number:
    print("YOU WIN !!!")

elif winning_number > guess_number:
    print("Too Low")

else:
    print("Too high")