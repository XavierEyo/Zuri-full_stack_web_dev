import random

print(f"\nR is Rock\nP is paper\nS is scissors\n")
player1_choice = input("choose one: R, P or S?")
choices = ["R", "P", "S"]
computer_choice = random.choice(choices)
print(f"\nYou chose {player1_choice}, computer chose {computer_choice}.\n")

if player_1_choice == computer_choice:
    print(f"Both players selected {player_1_choice}. It's a draw!")
elif player1_choice == "R":
    if computer_choice == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player1_choice == "P":
    if computer_choice == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player1_choice == "S":
    if computer_choice == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

