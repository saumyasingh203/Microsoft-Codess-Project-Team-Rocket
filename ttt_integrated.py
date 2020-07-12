import random
from flask import Flask, request, render_template, jsonify

board = [' '] * 10
turnNumber=0

def ChooseLetter():
    return ['X', 'O']


def make_move(board, letter, move):
    if Space_Free(board, move):#?
        board[move] = letter
    
def check_winner(bo, le):
#rows check
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or #columns check
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or # diagonals check
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def board_copy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def Space_Free(board, move):
    if board[move] == ' ':
        return True
    else:
        return False
    
def Player_Move(board):
    #print ("Choose a place")
    move = 0
    while not (move > 0 and move < 10) or not Space_Free(board, move):
        move = int(input())
    return move

def Random_Move(board, moves): #This function randomly chooses a spot from the list of possible spots provided, can be customized to make easy levels
    available_moves = []
    for i in moves: 
        if Space_Free(board, i):
            available_moves.append(i)

    if len(available_moves) != 0:
        return random.choice(available_moves)
    else:
        return None
    
def get_move(board, computer_letter,First_Player, turnNumber):
    if computer_letter == 'X':
        players_letter = 'O'
    else:
        players_letter = 'X'

     #attack
    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, computer_letter, i)
        if check_winner(copy, computer_letter):
            return i


    # defend
    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, players_letter, i)
        if check_winner(copy, players_letter):
            return i

    if First_Player == 'player':
        if Space_Free(board, 5):
            return 5

    if turnNumber == 2 and First_Player == 'player':
        move = Random_Move(board, [2, 4, 6, 8])
        if move != None:
            return move

   #CORNER
    move = Random_Move(board, [7, 9, 1, 3])
    if move != None:
        return move
   #CENTRE
    if Space_Free(board, 5):
        return 5

    # SIDES
    move = Random_Move(board, [2, 4, 6, 8])
    if move != None:
        return move
    
def move_l1(board, computer_letter):
    move = Random_Move(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    if move != None:
        return move

def move_l2(board, computer_letter):
    if computer_letter == 'X':
        players_letter = 'O'
    else:
        players_letter = 'X'

    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, computer_letter, i)
        if check_winner(copy, computer_letter):
            return i
    #DEFEND
    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, players_letter, i)
        if check_winner(copy, player_letter):
            return i

    move = Random_Move(board, [1, 2,3,4,5,6,7,8,9])
    if move != None:
        return move

def move_l3(board, computer_letter):
    if computer_letter == 'X':
        players_letter = 'O'
    else:
        players_letter = 'X'

    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, computer_letter, i)
        if check_winner(copy, computer_letter):
            return i
    #DEFEND
    for i in range(1, 10):
        copy = board_copy(board)
        make_move(copy, players_letter, i)
        if check_winner(copy, players_letter):
            return i

    move = Random_Move(board, [7, 9, 1, 3])
    if move != None:
        return move
    # CENTRE
    if Space_Free(board, 5):
        return 5

    move = Random_Move(board, [2,4,6,8])
    if move != None:
        return move

def get_move_draft(board, computerletter, theFirstPlayer, turnNumber, difficulty):
    if difficulty == 'l1':
        move = move_l1(board, computer_letter)
        return move
    if difficulty == 'l2':
        move = move_l2(board, computer_letter)
        return move
    if difficulty == 'l3':
        move = move_l3(board, computer_letter)
        return move
    if difficulty == 'l4':
        move = move_l4(board, computer_letter, First_Player, turnNumber)
        return move


def board_full(board):
    for i in range(1, 10):
        if Space_Free(board, i):
            return False
    return True

def update_turn(turnNumber):
    turnNumber += 1
    return turnNumber

def ttt(place):    
    player_letter, computer_letter = ChooseLetter()
    turn = 'player'
    First_Player = turn
    game_is_playing = True
         
    while game_is_playing:
        if turn == 'player':
            move = place
            make_move(board, player_letter, move)

            if check_winner(board, player_letter):
                game_is_playing = False
            if board_full(board):
                game_is_playing = False
            else:
                turn = 'computer'

        else:
            tn = update_turn(turnNumber)
            move = get_move(board, computer_letter, First_Player, tn)
            make_move(board, computer_letter, move)

            if check_winner(board, computer_letter):
                game_is_playing = False
            if board_full(board):
                game_is_playing = False
            else:
                turn = 'player'
                return(board)


        #break
        
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/index')
def playSwitch():
    return render_template('index.html')

@app.route('/number1', methods = ['GET','POST'])
def number1():
    answer=ttt(1)
    return jsonify(result=answer)

@app.route('/number2', methods = ['GET','POST'])
def number2():
    answer=ttt(2)
    return jsonify(result=answer)

@app.route('/number3', methods = ['GET','POST'])
def number3():
    answer=ttt(3)
    return jsonify(result=answer)

@app.route('/number4', methods = ['GET','POST'])
def number4():
    answer=ttt(4)
    return jsonify(result=answer)

@app.route('/number5', methods = ['GET','POST'])
def number5():
    answer=ttt(5)
    return jsonify(result=answer)

@app.route('/number6', methods = ['GET','POST'])
def number6():
    answer=ttt(6)
    return jsonify(result=answer)

@app.route('/number7', methods = ['GET','POST'])
def number7():
    answer=ttt(7)
    return jsonify(result=answer)

@app.route('/number8', methods = ['GET','POST'])
def number8():
    answer=ttt(8)
    return jsonify(result=answer)

@app.route('/number9', methods = ['GET','POST'])
def number9():
    answer=ttt(9)
    return jsonify(result=answer)

if __name__ == '__main__':
    app.run(debug=True)
   