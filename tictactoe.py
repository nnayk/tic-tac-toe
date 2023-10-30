"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board. If game has ended,
    returns None.
    """
    x_count, o_count = 0, 0
    for i in range(len(board)):
        if terminal(board):
            return None
        x_count, o_count = get_counts(board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    board[row][col] = player(board)


def winner(board):
    """
    Returns the winner of the game, if there is one. Else returns None.
    """
    result = utility(board)
    if result == 1:
        return X
    elif result == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    rows, cols = get_dimensions(board)
    return sum(get_counts) == (rows * cols)


def get_counts(board):
    """
    Returns the number of Xs and Os on the board.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    return x_count, o_count


def get_dimensions(board):
    """
    Returns dimesions (rows,columns) of the board.
    """
    return len(board), len(board[0])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    rows, cols = get_dimensions(board)
    # check all rows
    for row in board:
        if row.count(X) == len(row):
            return 1
        elif row.count(O) == len(row):
            return -1
    # check all columns
    for i in range(rows):
        col = [row[i] for row in board]
        if col.count(X) == len(col):
            return 1
        elif col.count(O) == len(col):
            return -1
    # check diagonals
    diagonal_1 = [board[i][i] for i in range(rows)]
    if len(set(diagonal_1)) == len(diagonal_1):
        return 1 if X in diagonal_1 else -1
    diagonal_2 = [board[i][cols - 1 - i] for i in range(rows)]
    if len(set(diagonal_2)) == len(diagonal_2):
        return 1 if X in diagonal_2 else -1
    # no winner
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
