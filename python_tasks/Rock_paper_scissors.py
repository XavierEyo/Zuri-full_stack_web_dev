import random

player= input("Enter a choice (r, p, s): ")
options = ["r", "p", "s"]
computer = random.choice(options)
print(f"\nYou chose {player1}, computer chose {computer}.\n")

if player == computer:
    print(f"Both players selected {player1}. It's a tie!")
elif player == "r":
    if computer == "s":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "p":
    if computer == "r":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "s":
    if computer == "p":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
