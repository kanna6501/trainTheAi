import tictactoe_nn

nn = tictactoe_nn.TicTacToeNN()

def introduce_game():
    print("\n" * 100)
    print("****************\nTic Tac Toe Game\n****************\n")
    print("Instructions:\nTo place an X or O at a spot, enter that spot's corresponding number.")
    print("\t\t|\t\t|")
    print("\t1\t|\t2\t|\t3\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print("\t4\t|\t5\t|\t6\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print("\t7\t|\t8\t|\t9\t")
    print("\t\t|\t\t|\n")


def print_board(positions):
    print("\t\t|\t\t|")
    print(f"\t{positions[0]}\t|\t{positions[1]}\t|\t{positions[2]}\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print(f"\t{positions[3]}\t|\t{positions[4]}\t|\t{positions[5]}\t")
    print("\t\t|\t\t|")
    print(" -------|-------|------- ")
    print("\t\t|\t\t|")
    print(f"\t{positions[6]}\t|\t{positions[7]}\t|\t{positions[8]}\t")
    print("\t\t|\t\t|\n")


def has_x_won(board):
    if "".join(board[:3]) == "XXX" or "".join(board[3:6]) == "XXX" or "".join(board[6:9]) == "XXX" or "".join(
            [board[0], board[3], board[6]]) == "XXX" or "".join([board[1], board[4], board[7]]) == "XXX" or "".join(
            [board[2], board[5], board[8]]) == "XXX" or "".join([board[0], board[4], board[8]]) == "XXX" or "".join(
            [board[2], board[4], board[6]]) == "XXX":
        return True
    return False


def has_o_won(board):
    if "".join(board[:3]) == "OOO" or "".join(board[3:6]) == "OOO" or "".join(board[6:9]) == "OOO" or "".join(
            [board[0], board[3], board[6]]) == "OOO" or "".join([board[1], board[4], board[7]]) == "OOO" or "".join(
            [board[2], board[5], board[8]]) == "OOO" or "".join([board[0], board[4], board[8]]) == "OOO" or "".join(
            [board[2], board[4], board[6]]) == "OOO":
        return True
    return False


def is_tie(board):
    return "" not in board


def run_game():
    # this part needs to be changed!!!!! create the object somewhere else!!!! this is only for testing purposes!!!!!
    list_each_board = []
    each_nnmove = []

    introduce_game()
    # if count is even, it's player 1's turn, if it's odd, it's player 2's turn
    count = 0
    board = [""] * 9
    first_player_marker = input("Player 1: Do you want to go first or second? (first/second) ").upper()
    while first_player_marker != "FIRST" and first_player_marker != "SECOND":
        first_player_marker = input("Please enter either \"first\" or \"second\": ").upper()
    if first_player_marker == "FIRST":
        first_player_marker = "X"
    else:
        first_player_marker = "O"
    second_player_marker = "X" if first_player_marker == "O" else "O"
    while True:
        if has_o_won(board):
            count = 0
            # only for temporary use, add a for loop for testing purposes
            #for number in range(5000):
            count = 0
            for each_board in list_each_board:
                nn.train_nn(each_board, each_nnmove[count])
                count += 1

        if has_x_won(board):
            print(f"Player X won.")
            break
        elif has_o_won(board):
            print(f"Player O won.")
            break
        elif is_tie(board):
            print("It is a tie, neither player wins.")
            break
        else:
            if first_player_marker == "X":
                is_input_error = False
                try:
                    if count % 2 == 0:
                        position = int(input(
                            f"Player {first_player_marker}, choose your position (1 through 9): ")) - 1
                    else:
                        position = nn.make_move(board) - 1
                        list_each_board.append(board)
                        each_nnmove.append(nn.make_move(board))
                except ValueError:
                    print("The position you enter must be an integer.")
                    is_input_error = True
                if not is_input_error:
                    if position < 0 or position > 8:
                        print("Please enter a position from 1 through 9.")
                    elif board[position] != "":
                        print("That position is already taken. Please choose a different position.")
                    else:
                        while board[position] == "":
                            if count % 2 == 0:
                                board[position] = first_player_marker
                            else:
                                board[position] = second_player_marker
                            print_board(board)
                            count += 1
            else:
                is_input_error = False
                try:
                    if count % 2 == 0:
                        position = nn.make_move(board) - 1
                        list_each_board.append(board)
                        each_nnmove.append(position)
                    else:
                        position = int(input(
                            f"Player {second_player_marker}, choose your position (1 through 9): ")) - 1
                except ValueError:
                    print("The position you enter must be an integer.")
                    is_input_error = True
                if not is_input_error:
                    if position < 0 or position > 8:
                        print("Please enter a position from 1 through 9.")
                    elif board[position] != "":
                        print("That position is already taken. Please choose a different position.")
                    else:
                        while board[position] == "":
                            if count % 2 == 0:
                                board[position] = first_player_marker
                            else:
                                board[position] = second_player_marker
                            print_board(board)
                            count += 1


while True:
    run_game()
    play_again = input("Do you want to play again? Enter \"yes\" or \"no\": ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Please enter either \"yes\" or \"no\": ").lower()
    if play_again == "no":
        break
