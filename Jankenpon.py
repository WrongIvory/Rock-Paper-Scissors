import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()
    if user_input =="q":
        break

    if user_input not in options:    
        continue

    random_number = random.randint(0, 2)
    #0 is to rock, 1 is to paper, 2 is to scissors
    computer_choice = options[random_number]
    print("Computer picked ", computer_choice + ".")

    if user_input == "rock" and computer_choice =="scissors":
        print("You win!")
        user_win += 1
    
    elif user_input == "paper" and computer_choice =="rock":
        print("You win!")
        user_win += 1
        
    elif user_input == "scissors" and computer_choice =="paper":
        print("You win!")
        user_win += 1
    
    elif user_input == computer_choice:
        print("It\'s a Tie!")
         
    else:
        print("You Lost!!")
        computer_win += 1

print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")
print("Nice Game!")
input("")