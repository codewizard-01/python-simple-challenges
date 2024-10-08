# Write a Rock, Paper, and Scissors game.
# Here the user will play with computer.

import random


def main():
    user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors\n "))
    computer_choice = random.randint(0, 2)
    set_emoji(user_choice, computer_choice)
    check_winner(user_choice, computer_choice)


def display_result(user_choice_emoji, computer_choice_emoji):
    print(f"Computer's Choice:  {computer_choice_emoji}")
    print(f"Your Choice: {user_choice_emoji}")


def set_emoji(user_choice, computer_choice):

    computer_choice_emoji = ""
    if computer_choice == 0:
        computer_choice_emoji = "🪨"
    elif computer_choice == 1:
        computer_choice_emoji = "📃"
    else:
        computer_choice_emoji = "✂"

    user_choice_emoji = ""
    if user_choice == 0:
        user_choice_emoji = "🪨"
    elif user_choice == 1:
        user_choice_emoji = "📃"
    else:
        user_choice_emoji = "✂"

    display_result(user_choice_emoji, computer_choice_emoji)


def check_winner(user_choice, computer_choice):
    if user_choice == 0 and computer_choice == 2:
        print("you won!")
    elif user_choice == 0 and computer_choice == 1:
        print("you lose!")
    elif user_choice == 1 and computer_choice == 0:
        print("you won!")
    elif user_choice == 1 and computer_choice == 2:
        print("you lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("you won!")
    else:
        print("draw")


main()