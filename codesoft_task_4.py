import random

choices = ["ROCK", "PAPER", "SCISSORS"]

play_again = "yes"

while play_again == "yes":
    user = input("\nChoose ROCK, PAPER, or SCISSORS: ").upper()
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif user == "ROCK" and computer == "SCISSORS":
        print("You win!")
    elif user == "SCISSORS" and computer == "PAPER":
        print("You win!")
    elif user == "PAPER" and computer == "ROCK":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()

print("\nThank you for playing with us!")
