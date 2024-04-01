import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Enter Rock/ Paper/ Scissors or Q to quit: ").lower() #getting user input and converting into lowercase

    if user_pick == "q":
        break

    if user_pick not in options:
        continue

    random_number = random.randint(0,2) #generating random numbers
    # rock - 0; paper - 1, scissors - 3

    computer_pick = options[random_number] #using the random number to choose the option of the index from the options list
    print("Computer picked", computer_pick +".")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_score += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You Won!")
        user_score += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_score += 1

    elif user_pick == computer_pick:
        print("It's a draw!")
        continue
    
    else:
        print("You Lost!")
        computer_score += 1

print("You won",user_score,"times.")
print("The Computer",computer_score,"times.")
print("Thanks for playing!!!")
