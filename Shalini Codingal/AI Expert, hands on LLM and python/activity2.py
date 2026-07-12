import random
from colorama import init, Fore, Style

init(autoreset=True)

# Winning positions
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]


def display_board(board):
    print()

    def colour(value):
        if value == "X":
            return Fore.RED + value + Style.RESET_ALL
        elif value == "O":
            return Fore.BLUE + value + Style.RESET_ALL
        return Fore.YELLOW + value + Style.RESET_ALL

    print(" " + colour(board[0]) + " | " + colour(board[1]) + " | " + colour(board[2]))
    print(Fore.CYAN + "---+---+---")
    print(" " + colour(board[3]) + " | " + colour(board[4]) + " | " + colour(board[5]))
    print(Fore.CYAN + "---+---+---")
    print(" " + colour(board[6]) + " | " + colour(board[7]) + " | " + colour(board[8]))
    print()


def player_choice():
    while True:
        choice = input(Fore.GREEN + "Choose X or O: ").upper().strip()
        if choice == "X":
            return "X", "O"
        elif choice == "O":
            return "O", "X"
        else:
            print("Enter only X or O.")


def player_move(board, symbol):
    while True:
        move = input("Enter position (1-9): ")

        if move.isdigit():
            move = int(move)

            if move >= 1 and move <= 9:
                if board[move - 1] not in ["X", "O"]:
                    board[move - 1] = symbol
                    break
                else:
                    print("That position is already used.")
            else:
                print("Choose a number from 1 to 9.")
        else:
            print("Invalid input.")


def ai_move(board, ai_symbol, player_symbol):

    # Try to win
    for i in range(9):
        if board[i] not in ["X", "O"]:
            temp = board[:]
            temp[i] = ai_symbol
            if check_win(temp, ai_symbol):
                board[i] = ai_symbol
                return

    # Block player
    for i in range(9):
        if board[i] not in ["X", "O"]:
            temp = board[:]
            temp[i] = player_symbol
            if check_win(temp, player_symbol):
                board[i] = ai_symbol
                return

    # Random move
    empty = []
    for i in range(9):
        if board[i] not in ["X", "O"]:
            empty.append(i)

    board[random.choice(empty)] = ai_symbol


def check_win(board, symbol):
    for a, b, c in win_conditions:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True
    return False


def check_full(board):
    for item in board:
        if item not in ["X", "O"]:
            return False
    return True


def tic_tac_toe():

    print(Fore.CYAN + "Welcome to Tic Tac Toe!")

    name = input(Fore.GREEN + "Enter your name: ").strip()

    if name == "":
        name = "Player"

    while True:

        board = [str(i) for i in range(1, 10)]

        player_symbol, ai_symbol = player_choice()

        turn = "Player"

        while True:

            display_board(board)

            if turn == "Player":

                player_move(board, player_symbol)

                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {name}! You won.")
                    break

                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw.")
                    break

                turn = "AI"

            else:

                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins.")
                    break

                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw.")
                    break

                turn = "Player"

        again = input("Play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    tic_tac_toe()