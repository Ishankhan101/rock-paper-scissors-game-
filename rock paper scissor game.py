# rock paper scissor game
import random
print("welcome to rock paper scissor game 😊")
choices = ["rock", "paper", "scissors"]
attempts = 3
attempt = 0
choice = input("enter your choice (rock/paper/scissors): ")
if choice not in choices:
    print("invalid choice. please choose rock, paper, or scissors.")
elif choice in choices:
    while attempt < attempts:
        user_choice = choice
        computer_choice = random.choice(choices)
        print(f"computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("it's a tie!🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("you win🤩!")
        else:
            print("you lose😂!")
        
        
        attempt = attempt + 1
        


