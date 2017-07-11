# Author : VARUN NANDU

import copy
import time
import math

# CONSTANTS:
COLUMNS=4
ROWS=4
n = 4
HUMANTOKEN="H"
COMPUTERTOKEN="C"

#---------------------------------------------------------------
def getEmptyBoard():
    board = [[[" . " for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
    return board

# #---------------------------------------------------------------
# def getFullBoard():
#     board = [[[" . " for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
#     board[0][0][-1] = "HS"
#     board[0][1][-1] = "CS"
#     board[0][2][-1] = "CS"
#     board[0][3][-1] = " . "
#     board[1][0][-1] = "HM"
#     board[1][1][-1] = "CM"
#     board[1][2][-1] = "HM"
#     board[1][3][-1] = "CM"
#     board[2][0][-1] = " . "
#     board[2][1][-1] = "HS"
#     board[2][2][-1] = "CL"
#     board[2][3][-1] = " . "
#     board[3][0][-1] = " . "
#     board[3][1][-1] = "CX"
#     board[3][2][-1] = " . "
#     board[3][3][-1] = "HM"
#
#
#
#
#
#     return board
#---------------------------------------------------------------
# Given : Board and token
# Returns: The count of Three in a row pieces for that token

def threeInARow(board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    count = 0
    for x in range(ROWS):  # Checks horizontal tokens
        for y in range(COLUMNS - 2):
            if (board[x][y][-1][0] == board[x][y + 1][-1][0] and board[x][y + 2][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    if ((y != 0 and board[x][y - 1][-1] == ' . ') or (y != (COLUMNS - 3) and (board[x][y + 3][-1] == ' . '))):
                        count += 1

    for x in range(ROWS - 2):  # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y][-1][0] and board[x + 2][y][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 3) and board[x + 3][y][-1] == ' . '):
                        count += 1

    for x in range(ROWS - 2):  # Checks diagional 1 tokens
        for y in range(COLUMNS - 2):
            if (board[x][y][-1][0] == board[x + 1][y + 1][-1][0] and board[x + 2][y + 2][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 3) and y != (COLUMNS - 3) and board[x + 3][y + 3][0] == ' . '):
                        count += 1

    for x in range(ROWS - 2):  # Checks diagional 2 tokens
        for y in range(2, COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y - 1][-1][0] and board[x + 2][y - 2][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 3) and y != 0 and board[x + 3][y - 3][-1] == ' . '):
                        count += 1
    return count

#-------------------------------------------------------------------------------------
# Given : A token Size and Board
# Returns: True iff the size of that token is already present on the Board

def checkPieceonBoard(token, s, board):
    flag = False
    for x in range(ROWS):
        for y in range(COLUMNS):
            if board[x][y][-1] == token + s:
                flag = True
            else:
                flag = False
    return flag
#------------------------------------------------------
# GIVEN: insert row, insert column, insert size, token and the current board
# RETURNS: True iff it is a valid insert move

def insertCheck(r, c, s, isHuman, board):
    flag = 0
    if isHuman:
        thisToken = HUMANTOKEN
        thatToken = COMPUTERTOKEN
    else:
        thisToken = COMPUTERTOKEN
        thatToken = HUMANTOKEN
    if board[r][c][-1][0] == thisToken:
        if s == "X" and (board[r][c][-1] == " . " or board[r][c][-1] == thisToken + "S" or board[r][c][
            -1] == thisToken + "M" or board[r][c][-1] == thisToken + "L"):
            return True
        elif s == "L" and (board[r][c][-1] == " . " or board[r][c][-1] == thisToken + "S" or board[r][c][
            -1] == thisToken + "M"):
            return True
        elif s == "M" and (board[r][c][-1] == " . " or board[r][c][-1] == thisToken + "S"):
            return True
        elif s == "S" and board[r][c][-1] == " . ":
            return True
        else:
            return False
    elif board[r][c][-1][0] == thatToken:
        flag = threeInARow(board, isHuman)
        if s == "X" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S" or board[r][c][-1] == thatToken + "M" or board[r][c][-1] == thatToken + "L") and checkPieceonBoard(thisToken, "X", board):
            return True
        elif s == "L" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S" or board[r][c][-1] == thatToken + "M") and checkPieceonBoard(thisToken, "L", board):
            return True
        elif s == "M" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S") and checkPieceonBoard(thisToken, "M", board):
            return True
        elif s == "X" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S" or board[r][c][-1] == thatToken + "M" or board[r][c][-1] == thatToken + "L") and not(checkPieceonBoard(thisToken, "X", board)) and flag >0:
            return True
        elif s == "L" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S" or board[r][c][-1] == thatToken + "M") and not(checkPieceonBoard(thisToken, "L", board)) and flag >0:
            return True
        elif s == "M" and (board[r][c][-1] == " . " or board[r][c][-1] == thatToken + "S") and not(checkPieceonBoard(thisToken, "M", board)) and flag > 0:
            return True
        elif s == "S" and board[r][c][-1] == " . ":
            return True
        else:
            return False
    else:
        return True



#------------------------------------------------------
# GIVEN: insert column, insert row, size, current board and token
# RETURNS: board with the given token inserted at the appropriate location with the appropriate size

def insert(c, r, s, boardUpdate,isHuman):
    if r == -1:
        return None # Column Full
    if isHuman:
        boardUpdate[r][c].append(HUMANTOKEN + s)
    else:
        boardUpdate[r][c].append(COMPUTERTOKEN + s)
    return boardUpdate


#------------------------------------------------------
# GIVEN: pick up column and row, drop column and row and current board
# RETURNS: Updated board
def update(pc, pr, dc, dr, boardUpdate):
    board = boardUpdate
    board[dr][dc].append(boardUpdate[pr][pc][-1])
    board[pr][pc].pop()
    return board

#------------------------------------------------------
# GIVEN: pick up column and row, drop column and row, token and current board
# RETURNS: True iff update is possible from dpickup location to drop location

def updateCheck(pr, pc, dr, dc, isHuman, gameBoard):
    if isHuman:
        thisToken = HUMANTOKEN
        thatToken = COMPUTERTOKEN
    else:
        thisToken = COMPUTERTOKEN
        thatToken = HUMANTOKEN
    if pr == dr and pc == dc:
        return False
    if gameBoard[pr][pc][-1][0] == gameBoard[dr][dc][-1][0]:
        if gameBoard[pr][pc][-1] == thisToken + "X" and (
                        gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thisToken + "S" or gameBoard[dr][dc][
                -1] == thisToken + "M" or gameBoard[dr][dc][-1] == thisToken + "L"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "L" and (
                    gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thisToken + "S" or gameBoard[dr][dc][-1] == thisToken + "M"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "M" and (gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thisToken + "S"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "S" and gameBoard[dr][dc][-1] == " . ":
            return True
        else:
            return False
    else:
        if gameBoard[pr][pc][-1] == thisToken + "X" and (
                        gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thatToken + "S" or gameBoard[dr][dc][
                -1] == thatToken + "M" or gameBoard[dr][dc][-1] == thatToken + "L"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "L" and (
                    gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thatToken + "S" or gameBoard[dr][dc][-1] == thatToken + "M"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "M" and (gameBoard[dr][dc][-1] == " . " or gameBoard[dr][dc][-1] == thatToken + "S"):
            return True
        elif gameBoard[pr][pc][-1] == thisToken + "S" and gameBoard[dr][dc][-1] == " . ":
            return True
        else:
            return False




#------------------------------------------------------
# GIVEN: size, board, token
# RETURNS: Number of small pieces of that token
def getSmallCount(s, board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    if s == "S":
        small_count = 1
    else:
        small_count = 0
    for c in range(COLUMNS):
        for r in range(ROWS):
            for j in range(len(board[r][c])):
                if board[r][c][j] == token + "S":
                    small_count += 1
    return small_count



#------------------------------------------------------
# GIVEN: size, board, token
# RETURNS: Number of medium pieces of that token

def getMediumCount(s, board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    if s == "M":
        medium_count = 1
    else:
        medium_count = 0
    for c in range(COLUMNS):
        for r in range(ROWS):
            for j in range(len(board[r][c])):
                if board[r][c][j] == token + "M":
                    medium_count += 1
    return medium_count




#------------------------------------------------------
# GIVEN: size, board, token
# RETURNS: Number of Large pieces of that token

def getLargeCount(s, board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    if s == "L":
        large_count = 1
    else:
        large_count = 0
    for c in range(COLUMNS):
        for r in range(ROWS):
            for j in range (len(board[r][c])):
                if board[r][c][j] == token + "L":
                    large_count += 1
    return large_count



#------------------------------------------------------
# GIVEN: size, board, token
# RETURNS: Number of xlarge pieces of that token

def getXLargeCount(s, board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    if s == "X":
        xlarge_count = 1
    else:
        xlarge_count = 0
    for c in range(COLUMNS):
        for r in range(ROWS):
            for j in range (len(board[r][c])):
                if board[r][c][j] == token + "X":
                    xlarge_count += 1
    return xlarge_count


#------------------------------------------------------
# GIVEN: A board list
# RETURNS: Board list to be displayed
def printBoard(board):

    for x in range(ROWS-1,-1,-1):
        print "%d " %x,
        for y in range(0,COLUMNS):

            print " | ",board[x][y][-1],
        print "|"
        print "     -------------------------"


#-----------------------------------------------------------
# Given: Board and Token
#Returns: list of all available actions from the current board

def getAvailableActions(board, isHuman):
    if isHuman:
        thisToken = HUMANTOKEN
        thatToken = COMPUTERTOKEN
    else:
        thisToken = COMPUTERTOKEN
        thatToken = HUMANTOKEN
    empty_count = 0
    my_count = 0
    their_count = 0
    s_count = 0
    m_count = 0
    l_count = 0
    x_count = 0

    dabba = []
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c][-1] == " . ":
                empty_count += 1
            elif board[r][c][-1][0] == thisToken:
                my_count+= 1
            elif board[r][c][-1][0] == thatToken:
                their_count+=1

    if empty_count == 16:
        for r in range(ROWS):
            for c in range(COLUMNS):
                dabba.append([True, -1, -1, r, c, thisToken + "S"])
                dabba.append([True, -1, -1, r, c, thisToken + "M"])
                dabba.append([True, -1, -1, r, c, thisToken + "L"])
                dabba.append([True, -1, -1, r, c, thisToken + "X"])
    for r in range(ROWS):
        for c in range(COLUMNS):
            dabba.append([True, -1, -1, r, c, thisToken + "S"])
            dabba.append([True, -1, -1, r, c, thisToken + "M"])
            dabba.append([True, -1, -1, r, c, thisToken + "L"])
            dabba.append([True, -1, -1, r, c, thisToken + "X"])

    for pr in range(ROWS):
        for pc in range(COLUMNS):
            for dr in range(ROWS):
                for dc in range(COLUMNS):
                    dabba.append([False, pr, pc, dr, dc, "HS"])

    for x in range(ROWS):
        for y in range(COLUMNS):
            if board[x][y][-1][1] == "X" and board[x][y][-1][0] == thisToken:
                x_count += 1
            if board[x][y][-1][1] == "L" and board[x][y][-1][0] == thisToken:
                l_count += 1
            if board[x][y][-1][1] == "M" and board[x][y][-1][0] == thisToken:
                m_count += 1
            if board[x][y][-1][1] == "S" and board[x][y][-1][0] == thisToken:
                s_count += 1
    if s_count == 3:
        for r in range(ROWS):
            for c in range(COLUMNS):
                dabba.remove([True, -1, -1, r, c, thisToken + "S"])
    if m_count == 3:
        for r in range(ROWS):
            for c in range(COLUMNS):
                dabba.remove([True, -1, -1, r, c, thisToken + "M"])
    if l_count == 3:
        for r in range(ROWS):
            for c in range(COLUMNS):
                dabba.remove([True, -1, -1, r, c, thisToken + "L"])
    if x_count == 3:
        for r in range(ROWS):
            for c in range(COLUMNS):
                dabba.remove([True, -1, -1, r, c, thisToken + "X"])
    SIZES = ["S", "M", "L", "X"]
    for x in range(ROWS):
        for y in range(COLUMNS):
            for s in SIZES:
                if my_count > 0 or their_count > 0:
                    if not insertCheck(x, y, s, False, board):
                        if [True, -1, -1, x, y, thisToken + s] in dabba: dabba.remove([True, -1, -1, x, y, thisToken + s])

    for pr in range(ROWS):
        for pc in range(COLUMNS):
            for dr in range(ROWS):
                for dc in range(COLUMNS):
                    if my_count> 0 or their_count > 0:
                        if not updateCheck(pr, pc, dr, dc, False, board):
                             dabba.remove([False, pr, pc, dr, dc, "HS"])
    return dabba




#---------------------------------------------------------------
#Given : Token, current board and action
#Returns: Next board state by taking the given action for the current token

def next_state(isHuman, board, action):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    ins, pr, pc, dr, dc, size = action
    if ins:
        return insert(dc, dr, size[1], board, token)
    else:
        return update(pc, pr, dc, dr, board)

#------------------------------------------------------------------
#Given : Current Board and depth
#Returns: Board after performing the optimal move computer can make by exploring the given depth

def getComputerMove(board, difficulty, move):
    start_time = time.clock()
    if move == 1:
        ins, pr, pc, dr, dc, size = minimax(board, difficulty, False)
    else:
        ins, pr, pc, dr, dc, size = alphaBetaPruning(board, difficulty, False)
    if ins:
        print time.clock() - start_time, "seconds to calculate the computer move"
        return insert(dc, dr, size[1], board, False)
    else:
        print time.clock() - start_time, "seconds to calculate the computer move"
        return update(pc, pr, dc, dr, board)

#------------------------------------------------------------------------
#Given: Board, depth and Token
#Returns: best action according to minimax algorithm running upto the given depth for the given token

def minimax(board, depth, isHuman):
    if isHuman:
        print "Human"
    else:
        possibleMoves = getAvailableActions(board, isHuman)
        bestValue = float("-inf")
        bestMove = possibleMoves[0]
        count = 0
        for x in possibleMoves:
            tempBoard = copy.deepcopy(board)
            next_state(isHuman, tempBoard, x)
            v = minimizer(x, tempBoard, depth)
            mv = math.fabs(v)
            if bestValue < mv:
                bestValue = mv
                bestMove = x
            count += 1
        return bestMove

# Given : a action x, current board, depth
# Returns: Minimizer score

def minimizer(x, board, depth):
    possibleMoves = getAvailableActions(board, False)
    if depth == 0 or len(possibleMoves) == 0 or isWinner(board):
        score = evaluationFunction(x, board, False) - evaluationFunction(x, board, True)
        return score
    bestValue = float("inf")
    for x in possibleMoves:
        tempBoard = copy.deepcopy(board)
        next_state(True, tempBoard, x)
        v = maximizer(x, tempBoard, depth - 1)
        if bestValue > v:
            bestValue = v
    return bestValue

# Given : a action x, current board, depth
# Returns: Maximizer score

def maximizer(x, board, depth):
    possibleMoves = getAvailableActions(board, False)
    if depth == 0 or len(possibleMoves) == 0 or isWinner(board):
        score = evaluationFunction(x, board, False) - evaluationFunction(x, board, True)
        return score
    bestValue = float("-inf")
    for x in possibleMoves:
        tempBoard = copy.deepcopy(board)
        next_state(False, tempBoard, x)
        v = minimizer(x, tempBoard, depth)
        if bestValue < v:
            bestValue = v
    return bestValue

#--------------------------------------------------------------


def alphaBetaPruning(board, depth, isHuman):
    if isHuman:
        print "Human"
    else:
        possibleMoves = getAvailableActions(board, isHuman)
        bestValue = -99999
        actualBestValue = -99999
        a = -99999
        b = 99999
        bestMove = possibleMoves[0]
        count = 0
        for x in possibleMoves:
            tempBoard = copy.deepcopy(board)
            next_state(isHuman, tempBoard, x)
            v = abminimizer(x, tempBoard, depth, a, b)

            modifiedV = math.fabs(v)

            if bestValue < modifiedV:
                bestValue = modifiedV
                bestMove = x
                actualBestValue = v
            if a < actualBestValue:
                a = actualBestValue
            count += 1

        return bestMove


def abminimizer(x, board, depth, a, b):
    possibleMoves = getAvailableActions(board, False)
    if depth == 0 or len(possibleMoves) == 0 or isWinner(board):
        score = evaluationFunction(x, board, False) - evaluationFunction(x, board, True)
        return score
    bestValue = 99999
    for x in possibleMoves:
        tempBoard = copy.deepcopy(board)
        next_state(True, tempBoard, x)
        v = abmaximizer(x, tempBoard, depth - 1, a, b)
        if bestValue > v:
            bestValue = v
        if b > bestValue:
            b = bestValue
        if bestValue < a:
            return bestValue
    return bestValue


def abmaximizer(x, board, depth, a, b):
    possibleMoves = getAvailableActions(board, False)
    if depth == 0 or len(possibleMoves) == 0 or isWinner(board):
        score = evaluationFunction(x, board, False) - evaluationFunction(x, board, True)
        return score
    bestValue = -99999
    for x in possibleMoves:
        tempBoard = copy.deepcopy(board)
        next_state(False, tempBoard, x)
        v = abminimizer(x, tempBoard, depth, a, b)
        if bestValue < v:
            bestValue = v
        if a < bestValue:
            a = bestValue
        if bestValue > b:
            return bestValue
    return bestValue


#---------------------------------------------------------------
# Given : Board and token
# Returns: The count of Four in a row pieces for that token
def fourInARow(board, isHuman):
    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    count = 0
    for x in range(ROWS):  # Checks horizontal tokens
        for y in range(COLUMNS - 3):
            if (board[x][y][-1][0] == board[x][y + 1][-1][0] and board[x][y + 2][-1][0] == board[x][y][-1][0] and board[x][y + 3][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    count += 1

    for x in range(ROWS - 3):  # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y][-1][0] and board[x + 2][y][-1][0] == board[x][y][-1][0] and board[x + 3][y][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    count += 1

    for x in range(ROWS - 3):  # Checks diagional 1 tokens
        for y in range(COLUMNS - 3):
            if (board[x][y][-1][0] == board[x + 1][y + 1][-1][0] and board[x + 2][y + 2][-1][0] == board[x][y][-1][0] and board[x + 3][y + 3][-1][0] ==
                board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    count += 1

    for x in range(ROWS - 3):  # Checks diagional 2 tokens
        for y in range(3, COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y - 1][-1][0] and board[x + 2][y - 2][-1][0] == board[x][y][-1][0] and board[x + 3][y - 3][-1][0] ==
                board[x][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    count += 1

    return count

#--------------------------------------------------------------------------------------------------------------------------------------------------

# Given : Board
# Returns: True iff there is a winner on the board

def isWinner(board):

    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 3):
            if (board[x][y][-1][0] == board[x][y+1][-1][0] and board[x][y+2][-1][0] == board[x][y][-1][0] and board[x][y+3][-1] == board[x][y][-1][0]):
                if (board[x][y][-1]== HUMANTOKEN or board[x][y][-1][0]==COMPUTERTOKEN):
                    return True
    for x in range(ROWS - 3): # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y][-1][0]==board[x+1][y][-1][0] and board[x+2][y][-1][0] == board[x][y][-1][0] and board[x+3][y][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0]== HUMANTOKEN or board[x][y][-1][0] == COMPUTERTOKEN):
                    return True
    for x in range(ROWS - 3): # Checks diagional 1 tokens
        for y in range(COLUMNS - 3):
            if (board[x][y][-1][0] == board[x+1][y+1][-1][0] and board[x+2][y+2][-1][0] == board[x][y][-1][0] and board[x+3][y+3][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == HUMANTOKEN or board[x][y][-1][0] == COMPUTERTOKEN):
                    return True
    for x in range(ROWS-3): # Checks diagional 2 tokens
        for y in range(3, COLUMNS):
            if (board[x][y][-1][0] == board[x+1][y-1][-1][0] and board[x+2][y-2][-1][0] == board[x][y][-1][0] and board[x+3][y-3][-1][0] == board[x][y][-1][0]):
                if (board[x][y][-1][0] == HUMANTOKEN or board[x][y][-1][0]==COMPUTERTOKEN):
                    return True

    return False

#------------------------------------------------------------------------------------------------------------------------------
# Given : Board and token
# Returns: The count of Two in a row pieces for that token

def twoInARow(board, isHuman):

    if isHuman:
        token = HUMANTOKEN
    else:
        token = COMPUTERTOKEN
    count = 0
    for x in range(ROWS):  # Checks horizontal tokens
        for y in range(COLUMNS - 1):
            if (board[x][y][-1][0] == board[x][y + 1][-1][0]):
                if (board[x][y][-1][0] == token):
                    if ((y != 0 and board[x][y - 1][-1] == ' . ') or (y != (COLUMNS - 2) and (board[x][y + 2][-1] == ' . '))):
                        count += 1

    for x in range(ROWS - 1):  # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 2) and board[x + 2][y][-1] == ' . '):
                        count += 1

    for x in range(ROWS - 1):  # Checks diagional 1 tokens
        for y in range(COLUMNS - 1):
            if (board[x][y][-1][0] == board[x + 1][y + 1][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 2) and y != (COLUMNS - 2) and board[x + 2][y + 2][-1] == ' . '):
                        count += 1

    for x in range(ROWS - 2):  # Checks diagional 2 tokens
        for y in range(1, COLUMNS):
            if (board[x][y][-1][0] == board[x + 1][y - 1][-1][0]):
                if (board[x][y][-1][0] == token):
                    if (x != (ROWS - 2) and y != 0 and board[x + 2][y - 2][-1] == ' . '):
                        count += 1

    return count

#---------------------------------------------------------------
#Given: an action, board and token
#Returns: A score for the available action in the current board

def evaluationFunction(x, board, isHuman):
    if isHuman:
        thisToken = HUMANTOKEN
        thatToken = COMPUTERTOKEN
    else:
        thisToken = COMPUTERTOKEN
        thatToken = HUMANTOKEN
    ins, pr, pc, dr, dc, size = x

    FourInARow = 1000000
    ThreeInARow = 50000
    TwoInARow = 10000
    general = 5000
    if threeInARow(board, thisToken) > 1:
        ThreeInARow = 15 * ThreeInARow
    if threeInARow(board, thatToken) and size[1] == "X" and dr == 2 and dc == 2:
        ThreeInARow = 9 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "X" and dr == 1 and dc == 1:
        ThreeInARow = 8 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "X" and (dr == 0 and pc == 0) or (dr == 3 and dc == 3):
        ThreeInARow = 7 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "L" and dr == 2 and dc == 2:
        ThreeInARow = 6 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "L" and dr == 1 and dc == 1:
        ThreeInARow = 5 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "L" and (dr == 0 and pc == 0) or (dr == 3 and dc == 3):
        ThreeInARow = 4 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "M"  and dr == 2 and dc == 2:
        ThreeInARow = 3 * ThreeInARow
    elif threeInARow(board, thatToken) and size[1] == "M":
        ThreeInARow = 2 * ThreeInARow

    if twoInARow(board, thisToken) == 4:
        TwoInARow = 4 * TwoInARow
    elif twoInARow(board, thisToken) == 3:
        TwoInARow = 3 * TwoInARow
    elif twoInARow(board, thisToken) == 2:
        TwoInARow = 2 * TwoInARow

    if size[1] == "X":
        general = 4 * general
    elif size[1] == "L":
        general = 3 * general
    elif size[1] == "M":
        general = 2 * general

    return (FourInARow*fourInARow(board,isHuman)) + (ThreeInARow*threeInARow(board,isHuman))+(TwoInARow*twoInARow(board,isHuman) + general)

# start_time = time.clock()
# printBoard(getFullBoard())
# m = alphaBetaPruning(getFullBoard(),2, False)
# print "action is", m
# print time.clock() - start_time, "seconds to calculate the computer move"
#---------------------------------------------------------------
def main():
    print "Welcome to Gobblet Gobblers"
    print "Please choose a difficulty level -> 0:Easy 1:Medium 2:Hard 3:Expert"
    difficulty=int(input())
    print "Human Player plays first"
    print "Difficulty level chosen is ",difficulty
    print "We will use 1) MiniMax Algorithm or 2) alphabetapruning"
    move = int(input())
    print "Human Plays First"
    firstPlayer=1
    print "%d player's move"%firstPlayer
    gameBoard=getEmptyBoard()
    if firstPlayer==2:
        getComputerMove(gameBoard,difficulty, move)
    while (not isWinner(gameBoard)):
        print "Human Move:"
        print printBoard(gameBoard)
        print "Enter 0. To Move an Existing Piece or 1. To insert a new piece"
        choice = int(input())
        if(choice == 1):
            print "Choose a column from ",
            enteredColumn= int(input())
            print "Choose a row from ",
            enteredRow = int(input())
            enteredSize = raw_input("Choose a size from [S, M, L, X]")
        else:
            print "Pick up Column"
            pickupColumn = int(input())
            print "Pick up Row"
            pickupRow = int(input())
            print "Drop Column"
            dropColumn = int(input())
            print "Drop Row"
            dropRow = int(input())
        s = getSmallCount(enteredSize, gameBoard, True)
        m = getMediumCount(enteredSize, gameBoard, True)
        l = getLargeCount(enteredSize, gameBoard, True)
        x = getXLargeCount(enteredSize, gameBoard, True)
        flag = True
        if s<=3 and m<=3 and l<=3 and x<=3:
           flag = True
        else:
            print "You have exhausted your available count of any of the sizes. You only have 3 of each"
            flag = False
        if (flag == True and choice == 1 and insertCheck(enteredRow, enteredColumn, enteredSize, True, gameBoard) == True):
            insert(enteredColumn, enteredRow, enteredSize, gameBoard,True)
            print printBoard(gameBoard)
            if not isWinner(gameBoard):
                print "Computer Move"
                getComputerMove(gameBoard,difficulty, move)
        elif (choice == 0 and gameBoard[pickupRow][pickupColumn][-1] != " . " and updateCheck(pickupRow, pickupColumn, dropRow, dropColumn, True, gameBoard)):
            update(pickupColumn, pickupRow, dropColumn, dropRow, gameBoard)
            print printBoard(gameBoard)
            if not isWinner(gameBoard):
                print "Computer Move"
                getComputerMove(gameBoard, difficulty, move)
        else:
            print "\nPlease choose a valid entry"
    if isWinner(gameBoard):
        if not fourInARow(gameBoard, True) > 1:
            print "Human wins!!!"
        else:
            print printBoard(gameBoard)
            print "Computer Wins!!!"
    else:
        print "Game has been drawn"

        
if __name__ == '__main__':
    main()
