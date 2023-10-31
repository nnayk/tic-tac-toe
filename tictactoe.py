"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    Returns a new board that results from making move (i, j) on the board.
    Raises an exception if action is not valid.
    """
    newBoard = deepcopy(board)
    row, col = action
    if not valid_bounds(row, col, board):
        raise Exception(f"Invalid action ({row},{col})")
    newBoard[row][col] = player(board)
    return newBoard


def valid_bounds(row, col, board):
    """
    Returns True if row and col are within the bounds of the board.
    """
    rows, cols = get_dimensions(board)
    return (row >= 0 and row < rows) and (col >= 0 and col < cols)


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
    win = winner(board)
    return True if win else None


def get_counts(board):
    """
    Returns the number of Xs and Os on the board.
    """
    x_count, o_count = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    print(f"get_counts: x_count = {x_count}, o_count = {o_count}")
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
            print("r1")
            return 1
        elif row.count(O) == len(row):
            print("r2")
            return -1
    # check all columns
    for i in range(rows):
        col = [row[i] for row in board]
        if col.count(X) == len(col):
            print("c1")
            return 1
        elif col.count(O) == len(col):
            print("c2")
            return -1
    # check diagonals
    diagonal_1 = [board[i][i] for i in range(rows)]
    if diagonal_1.count(X) == len(diagonal_1):
        print("d1")
        return 1
    elif diagonal_1.count(O) == len(diagonal_1):
        print("d2")
        return -1
    diagonal_2 = [board[i][rows - 1 - i] for i in range(rows)]
    if diagonal_2.count(X) == len(diagonal_2):
        print("d3")
        return 1
    elif diagonal_2.count(O) == len(diagonal_2):
        print("d4")
        return -1
    # no winner
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Returns None for a terminal board.
    """
    if terminal(board):
        return None, None

    def helper(currBoard):
        if terminal(currBoard):
            return utility(currBoard), None
        possibleActions = actions(currBoard)
        currPlayer = player(currBoard)
        bestScore = None
        bestAction = None
        # try each action, and return the best one at each step.
        # utilize alpha beta pruning to avoid exploring unnecessary
        # actions
        for action in possibleActions:
            newBoard = result(currBoard, action)
            print(f"recursing on {newBoard}")
            score = helper(newBoard)[0]
            print(f"score = {score}")
            # if max_score(currPlayer, score):
            #     bestAction = action
            #     bestScore = score
            #     break
            if bestScore is None:
                bestAction = action
                bestScore = score
            elif currPlayer == X and score > bestScore:
                bestAction = action
                bestScore = score
            elif currPlayer == O and score < bestScore:
                bestAction = action
                bestScore = score
        print(f"best score = {bestScore}, best action = {bestAction}")
        return (bestScore, bestAction)

    data = helper(board)
    print("post minimax: ", data)
    return data[1]


def max_score(currPlayer, score):
    """
    Returns True if the score is the best score for the current player.
    """
    return (currPlayer == X and score == 1) or (currPlayer == O and score == -1)
