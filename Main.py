import pprint

"""7 columns, 6 rows"""
"""Line of 4 wins, vertically, horizontally, diagonally"""

BOARD_SIZE = 6, 7
LINE_LENGTH = 4
PIECE_ONE = chr(int('2B24', 16))  # Unicode for white square
PIECE_TWO = chr(int('25EF', 16))  # Unicode for black square
EMPTY_SQUARE = " "


def create_board(size=BOARD_SIZE):
    """Create the board"""
    board = [[EMPTY_SQUARE for __ in range(size[1])] for _ in range(size[0])]
    return board


def print_board(board):
    for row in board:
        line = "|"
        for square in row:
            line += " " + square + " |"
        print(line)
        # print("-" * (BOARD_SIZE[1] * 4 + 1))


def get_column(board, column):
    return [row[column] for row in board]


def place_piece(board, column, player):
    current_col = get_column(board, column)
    move_index = current_col[::-1].index(EMPTY_SQUARE)
    board[-1 - move_index][column] = player


def player_input(board):
    while True:
        column = input("Choose a column to place a piece!")
        if column in [str(x) for x in range(1, (BOARD_SIZE[1] + 1))]:
            col_index = int(column) - 1
            if board[0][col_index] != EMPTY_SQUARE:
                print("This column is full!")
                continue
            return col_index
        print("Incorrect input!")


def win_con(board):
    for row in board:
        if PIECE_ONE in row:
            col_index = row.index(PIECE_ONE)
            potential_line = row[col_index:col_index + LINE_LENGTH]
            if potential_line.count(PIECE_ONE) == LINE_LENGTH:
                return True



if __name__ == "__main__":
    player = PIECE_ONE
    board = create_board()
    print_board(board)
    while True:
        place_piece(board, player_input(board), player)
        print_board(board)
        print(win_con(board))