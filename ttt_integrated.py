import random
from flask import Flask, request, render_template, jsonify, json, redirect
import pymongo
client = pymongo.MongoClient("mongodb+srv://tictac:12345@cluster0.rqmzw.mongodb.net/tictac?retryWrites=true&w=majority")
db = client.test
# print(db)
users = db.users
currentUser = {}

board = [' '] * 10
turnNumber = 0
isWinner = 0
win = [0, 0, 0]
level=0
status=2 #-1 -> loss; 0 -> tie; 1 -> win
turn = 'player'

def addUpdateUser(name, email, message, score = 0):
    userDocument = {
    "name": name,
    "email": email,
    "message": message,
    "score":score
    }
    global currentUser
    if(email not in [x['email'] for x in users.find({}, {"_id":0, "email":1})]):
        users.insert_one(userDocument)
        user = users.find_one({'email':email}, {"_id":0})
        currentUser = user
    else:
        users.update_one({"email":email}, {"$set":{"name":name, "message":message, "score":score}})
        user = users.find_one({'email':email}, {"_id":0})
        currentUser = user
    print(currentUser)
    
def update_AI():
    global turn
    turn = 'computer'
    global board
    board = [' '] * 10
    global turnNumber
    turnNumber = 0
    global isWinner
    isWinner = 0
    global win
    win = [0, 0, 0]
    global status
    status=2
    
def update_human():
    global turn
    turn = 'player'
    global board
    board = [' '] * 10
    global turnNumber
    turnNumber = 0
    global isWinner
    isWinner = 0
    global win
    win = [0, 0, 0]
    global status
    status=2
    

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
    
def update_winner(bo, le):
#rows check
    global win
    global isWinner
    if (bo[7] == le and bo[8] == le and bo[9] == le) :
        win = [7, 8, 9]
        isWinner = 1
        return True
    if (bo[4] == le and bo[5] == le and bo[6] == le) :
        win = [4, 5, 6]
        isWinner = 1
        return True
    if (bo[1] == le and bo[2] == le and bo[3] == le) :
        win = [1, 2, 3]
        isWinner = 1
        return True
    if (bo[7] == le and bo[4] == le and bo[1] == le) :
        win = [7, 4, 1]
        isWinner = 1
        return True
    if (bo[8] == le and bo[5] == le and bo[2] == le) :
        win = [8, 5, 2]
        isWinner = 1
        return True
    if (bo[9] == le and bo[6] == le and bo[3] == le) :
        win = [9, 6, 3]
        isWinner = 1
        return True
    if (bo[7] == le and bo[5] == le and bo[3] == le) :
        win = [7, 5, 3]
        isWinner = 1
        return True
    if (bo[9] == le and bo[5] == le and bo[1] == le) :
        win = [9, 5, 1]
        isWinner = 1
        return True
    
   

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
    
def move_l4(board, computer_letter,First_Player, tn):
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

    if tn == 2 and First_Player == 'player':
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
        if check_winner(copy, players_letter):
            return i

    move = Random_Move(board, [1,2,3,4,5,6,7,8,9])
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

def get_move_draft(board, computer_letter, First_Player, tn, difficulty):
    if difficulty == 1:
        move = move_l1(board, computer_letter)
        return move
    if difficulty == 2:
        move = move_l2(board, computer_letter)
        return move
    if difficulty == 3:
        move = move_l3(board, computer_letter)
        return move
    if difficulty == 4:
        move = move_l4(board, computer_letter, First_Player, tn)
        return move


def board_full(board):
    for i in range(1, 10):
        if Space_Free(board, i):
            return False
    return True

def update_turn(turnNumber):
    turnNumber += 1
    return turnNumber

##main function##

def ttt(place):    
    player_letter, computer_letter = ChooseLetter()

    if check_winner(board, computer_letter):
        return board
    if check_winner(board, player_letter):
        return board
    
    global turn
    First_Player = turn
    game_is_playing = True
    global status
         
    while game_is_playing:
        if turn == 'player':
            move = place
            make_move(board, player_letter, move)

            if check_winner(board, player_letter):
                game_is_playing = False
                return(board)
            if board_full(board):
                status=0
                game_is_playing = False
                return(board)
            else:
                turn = 'computer'

        else:
            tn = update_turn(turnNumber)
            move = get_move_draft(board, computer_letter, First_Player, tn, level)
            make_move(board, computer_letter, move)

            if check_winner(board, computer_letter):
                game_is_playing = False
                return(board)
            if board_full(board):
                status=0
                game_is_playing = False
                return(board)
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

@app.route('/scores')
def getScores():
    print (users.estimated_document_count())
    l = [{"name":x['name'],"score": x['score']} for x in users.find().sort('score', -1)]
    scores = json.dumps(l)
    # print(scores)
    return scores

@app.route('/bind-user', methods = ['POST'])
def bindUser():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        score = request.form['score']
        addUpdateUser(name, email, message, score)
        return redirect('index')

@app.route('/get-user')
def getUser():
    # print("The current user is:", currentUser)
    return json.dumps(currentUser)
    

@app.route('/update-score', methods = ['POST'])
def updateScore():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        score = request.form['score']
        addUpdateUser(name, email, message, score)
        return "done"


@app.route('/database')
def getDB():
    return render_template('database.html')

@app.route('/get-user-data')
def getDBData():
    data =  [x for x in users.find({}, {"_id":0})]
    return json.dumps(data)

##function calls to play game##

@app.route('/number1', methods = ['GET','POST'])
def number1():
    answer = ttt(1)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number2', methods = ['GET','POST'])
def number2():
    answer = ttt(2)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number3', methods = ['GET','POST'])
def number3():
    answer = ttt(3)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number4', methods = ['GET','POST'])
def number4():
    answer = ttt(4)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number5', methods = ['GET','POST'])
def number5():
    answer = ttt(5)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number6', methods = ['GET','POST'])
def number6():
    answer = ttt(6)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number7', methods = ['GET','POST'])
def number7():
    answer = ttt(7)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number8', methods = ['GET','POST'])
def number8():
    answer = ttt(8)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)

@app.route('/number9', methods = ['GET','POST'])
def number9():
    answer = ttt(9)
    global status
    if (update_winner(board, 'X') == True) :
        status = 1
    if (update_winner(board, 'O') == True) :
        status = -1
    return jsonify(status=status, result=answer, hasWon=isWinner, winBoard=win)


##Assigning Levels##

@app.route('/level1', methods = ['GET','POST'])
def level1():
    global level
    level = 1
    return jsonify(board)

@app.route('/level2', methods = ['GET','POST'])
def level2():
    global level
    level = 2
    return jsonify(board)
    
@app.route('/level3', methods = ['GET','POST'])
def level3():
    global level
    level = 3
    return jsonify(board)
    
@app.route('/level4', methods = ['GET','POST'])
def level4():
    global level
    level = 4
    return jsonify(board)

##AI start and Human Start##
@app.route('/startAI', methods = ['GET','POST'])
def startAI():
    update_AI()
    return jsonify(board)

@app.route('/startHuman', methods = ['GET','POST'])
def startHuman():
    update_human()
    return jsonify(board)


if __name__ == '__main__':
    app.run(debug=True)
