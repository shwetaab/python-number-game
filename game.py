import random
#test2
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors.")
print("Type quit to exit.")

while True:
    user_choice = input("\nYour choice: ").lower().strip()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    #test_comment_by_abhinav

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
