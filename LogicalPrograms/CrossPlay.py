current_player = "X"
winner=None
game=True
position=0
board = [" "for x in range(10)]

#Printing The Empyt Board
def printBoard():
    print("-------")
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("-------")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("-------")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")
    print("-------")
 
# Asking The Player To Select Choose A Position On Board
def playGame(player):
    try:
        print(player + " Should Play Now")
        position = int(input("Choose A position From 1-9:"))
        position!=0
        
        if " " in board[position]: 
            board[position] = player
        else:
            print("Position Is Already Occupied")
    except Exception as err:
        print("Enter A Valid Position::",err)
    printBoard()

 #Switing The Players Turn   
def turn():
    global current_player
    if current_player == "X":
        current_player = 'O'
    elif current_player == "O":
        current_player = "X"

#Checking For Winner        
def win_check():
    global winner
    global game
    if board[1] == board[2] == board[3] != ' ': #Row Check
        game=False
        return board[1]
    elif board[4] == board[5] == board[6] != ' ': #Row Check
        game=False
        return board[4]
    elif board[7] == board[8] == board[9] != ' ': #Row Check
        game=False
        return board[7]
    elif board[1] == board[4] == board[7] != ' ': #Column Check
        game=False
        return board[1]
    elif board[2] == board[5] == board[8] != ' ': #Column Check
        game=False
        return board[2]
    elif board[3] == board[6] == board[9] != ' ': #Column Check
        game=False
        return board[3]
    elif board[1] == board[5] == board[9] != ' ': #Diagonal Check
        game=False
        return board[1]
    elif board[3] == board[5] == board[7] != ' ': #Diagonal Check
        game=False
        return board[3]
    return False

def check_draw():
    global game
    if " " not in board:
        game=False
        return True
    else:
        return None     

#Checking If It's A Draw Or Win 
def board_full():
    global game
    winner=win_check()
    if winner == "X" or winner == "O":
        game=False
        print("winner Is:", winner)
    elif winner == None:
        print("It's ADraw")

#Calling All The Functions Here        
def cross_game():
    global game
    printBoard()    
    while game:
        playGame(current_player)
        win_check()
        turn()
        board_full()
        check_draw()
cross_game()  #play the game