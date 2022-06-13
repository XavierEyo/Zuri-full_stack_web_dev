import random

player1_choice = input("choose one: Rock, Paper or Scissors?")
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
print(f"\nYou chose {player1_choice}, computer chose {computer_choice}.\n")

if player_1_choice == computer_choice:
    print(f"Both players selected {player_1_choice}. It's a draw!")
elif player1_choice == "Rock":
    if computer_choice == "Scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player1_choice == "Paper":
    if computer_choice == "Rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player1_choice == "Scissors":
    if computer_choice == "Paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

