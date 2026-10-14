import random
while True:
    user_action = input("Choose rock, paper, or scissors: ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You: {user_action} | Computer: {computer_action}")
    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid choice!")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break
