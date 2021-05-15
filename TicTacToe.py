import random

def print_board(board):
    print(" {} | {} | {} ".format(board[1],board[2],board[3]) )
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4],board[5],board[6]) )
    print("---+---+---")
    print(" {} | {} | {} ".format(board[7],board[8],board[9]) )


def winCheck(board):
    if board[1] == board[2] == board[3] != ' ':
        return True
    if board[4] == board[5] == board[6] != ' ':
        return True
    if board[7] == board[8] == board[9] != ' ':
        return True
    if board[1] == board[4] == board[7] != ' ':
        return True
    if board[2] == board[5] == board[8] != ' ':
        return True
    if board[3] == board[6] == board[9] != ' ':
        return True
    if board[1] == board[5] == board[9] != ' ':
        return True
    if board[3] == board[5] == board[7] != ' ':
        return True
    return False


def is_rePlay():
    rePlay = input("Ban co muon choi lai khong : y/n ?")
    if rePlay == 'y' :
        return True
    if rePlay == 'n' :
        return False

def fullCheck(board) :
    return len([x for x in board if x == ' ']) == 1


def moveCheck(board, position):
    if board[int(position)] != ' ':
        return False
    return True


def playerMove(board):
    choice = input("Vui long chon nuoc di cua ban tu 1-9 :")
    while not moveCheck(board,choice) :
        choice = input("Vui long nhap lai")
    return choice
    

def computerMove(board) :
    choice = random.randint(1,9)
    while not moveCheck(board,choice):
        choice = random.randint(1,9)
    return choice
    

def drawBoard(board, position,mark) :
    board[int(position)] = mark



if __name__ == "__main__" :
    board = [' ']*10
    player = 'X'
    computer = 'O'
    win = False
    while True:

        while not fullCheck(board):
            positionPlayer = playerMove(board)
            drawBoard(board, positionPlayer, player)
            if winCheck(board) :
                print("Ban thang!")
                print_board(board)
                break

            positionComputer = computerMove(board)
            drawBoard(board, positionComputer, computer)
            print_board(board)
            if winCheck(board) :
                print("May thang!")
                print_board(board)
                break
        if not is_rePlay():
            break
        else:
            win = False
            board = [' ']*10

            

            


