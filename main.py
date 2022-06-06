import random
import message  # module containing function to display instructions


# checks if player is ready to start game
def to_start():
    ready_or_not = input("Are you ready to start?---")
    # convert entered string to lowercase
    ready_or_not = ready_or_not.lower()

    if (ready_or_not == "yes"):
        # if user is ready call module function to display instructions and to start game
        message.instructions()
        start_game()
    elif (ready_or_not == "no"):
        # exit game if user is not ready or ask again
        to_quit()
    else:
        print("Invalid option, please try again")
        to_start()


# function to start the game
def start_game():
    choices = ['rock', 'paper', 'scissors']
    print("Pick your move: 'R', 'P', 'S'")
    player_choice = input("your move: ")
    # Computer chooses randomly from the list 'choices'
    computer_move = random.choice(choices)

    # convert entered string to lowercase
    player_choice = player_choice.lower()

    # name all player moves
    if (player_choice == "r"):
        player_move = "rock"
    elif(player_choice == "p"):
        player_move = "paper"
    elif (player_choice == "s"):
        player_move = "scissors"
    else:
        while (player_choice not in choices):
            print("Invalid move, please follow the instructions carefully")
            start_game()
            break

    # check/compare moves to get result
    if (player_move == computer_move):
        print("Player(%s) : CPU(%s)" % (player_move, computer_move))
        print("It is a tie\n")
    elif (player_move == "rock"):
        if(computer_move == "paper"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You lose\n")
        if(computer_move == "scissors"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You win\n")
    elif (player_move == "paper"):
        if(computer_move == "rock"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You win\n")
        if(computer_move == "scissors"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You lose\n")
    elif (player_move == "scissors"):
        if(computer_move == "rock"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You lose\n")
        if(computer_move == "paper"):
            print("Player(%s) : CPU(%s)" % (player_move, computer_move))
            print("You win\n")

    play_again()


# function to quit game if not ready
def to_quit():
    quit = input("do you want to quit the game (yes/no): ")
    quit = quit.lower()
    if (quit == "yes"):
        print("Bye, please come again soon.")
        exit()
    elif(quit == 'no'):
        to_start()
    else:
        print("Invalid option, please try again")
        to_quit()


# function to play again
def play_again():
    quit = input("do you want to play again (yes/no): ")
    quit = quit.lower()
    if (quit == "no"):
        print("Bye!")
        exit()
    elif(quit == 'yes'):
        start_game()
    else:
        print("Invalid option, please try again")
        play_again()


# Program begins
to_start()
