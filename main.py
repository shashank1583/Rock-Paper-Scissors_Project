#  import the module you’ll use to simulate the computer’s choices:
import random

#scoring
user_wins = 0
computer_wins = 0

while True:

    # take the user input
    user_action = input("Enter a choice (rock, paper, scissors): ")

    # Define the possible choices and let the computer choose one of them randomly
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    # Determine a Winner i.e. Implement the logic
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == 'rock':
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1
    else:
        print("Your choice doesnt exist, You loose")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break

print("\n")    
print("Thank you for playing .!")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
