import random

def get_user_choice():
    # Prompt the user to choose rock, paper, or scissors
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    # Generate a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the user's choice and the computer's choice
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("----------------------------")

        # Get user's choice
        user_choice = get_user_choice()

        # Get computer's choice
        computer_choice = get_computer_choice()

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # Display the result
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("\nScores:")
        print("You:", user_score)
        print("Computer:", computer_score)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
