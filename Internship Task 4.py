#internship task 4
#ROCK PAPER SCISSSORS

import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if _name_ == "_main_":
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break