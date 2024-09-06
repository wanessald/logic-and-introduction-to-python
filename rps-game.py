import os
import random

options = ['rock', 'spock', 'paper', 'lizard', 'scissors']

def computer_chooses(options):
    return random.choice(options)

def compare_choices(player_choice, computer_choice):
    player_index = options.index(player_choice)
    computer_index = options.index(computer_choice)
    
    index_of_one_position_back = (player_index - 1) % len(options)
    index_of_two_positions_back = (player_index - 2) % len(options)

    if computer_index == index_of_one_position_back or computer_index == index_of_two_positions_back:
        return "Player Wins!"
    elif player_index == computer_index:
        return "Player and computer tie!"
    else:
        return "Computer Wins!"

def start_game():
    os.system('cls')

    continue_game = True
        
    while continue_game:
            player_input = str(input(
            "Choose your weapon: \n"
            "[1] - Rock\n"
            "[2] - Spock\n"
            "[3] - Paper\n"
            "[4] - Lizard\n"
            "[5] - Scissors\n"
            "Your choice: "
        ))
            if player_input.lower() in options:
                computer_choice = computer_chooses(options)
                print(f"\nPlayer chooses {player_input.capitalize()}.")
                print(f"Computer chooses {computer_choice.capitalize()}.")

                result = compare_choices(player_input, computer_choice)
                print(result)
            else:
                print("Enter a valid option!")

            user_choice = input("\nPress X to exit\nPress Y to continue").upper()

            if user_choice == 'X':
                continue_game = False
                print('Thanks for playing. See you later!')
            elif user_choice == 'Y':
                continue_game = True
            else:
                print('Invalid option!')

start_game()
