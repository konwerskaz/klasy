

import random
howmany = int(input("How many games do you want to play?: "))
round = 0
wins = 0

while howmany > 0:
     user_choice = input("What is your choice (rock, paper, scissors):")

     all_choices = ["rock", "paper", "scissors"]
     computer_choice = random.choice(all_choices)
     all_messages = {"p-r": "Paper covers rock!", "r-s": "Rock smashes scissors!", "s-p": "Scissors cuts paper!"}
     print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

     if user_choice == computer_choice:
        print("It's a tie!")
        round += 1
        if howmany == round:
            print(f"You won {wins} times in {round} games!")
            break

     elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print(f"{all_messages['r-s']} You win!")
            round += 1
            wins += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break

        else:
            print(f"{all_messages['p-r']} You lose.")
            round += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break

     elif user_choice == 'paper':
        if computer_choice == 'rock':
            round += 1
            print(f"{all_messages['p-r']}  You win!")
            wins += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break

        else:
            print(f"{all_messages['s-p']} You lose.")
            round += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break

     elif user_choice == 'scissors':
        if computer_choice == 'paper':
            round += 1
            print(f"{all_messages['s-p']} You win!")
            wins += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break

        else:
            print(f"{all_messages['r-s']} You lose.")
            round += 1
            if howmany == round:
                print(f"You won {wins} times in {round} games!")
                break


