#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def draw_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def difficulty_level():
    difficulty = ''
    while not (difficulty == 'l1' or difficulty == 'l2' or difficulty == 'l3' or difficulty == 'l4'):
        print("Please enter a difficulty level: l1, l2, l3, or l4")
        difficulty = input()
    return difficulty

def ChooseLetter():
    print("Choose X or O")
    letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def First():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

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
    print ("Choose a place")
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
    
def move_l4(board, computer_letter,First_Player, turnNumber):
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

def get_move(board, computerletter, theFirstPlayer, turnNumber, difficulty):
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
print("Welcome!")

while True:
    difficulty = difficulty_level()
    board = [' '] * 10
    player_letter, computer_letter = ChooseLetter()
    turn = First()
    First_Player = turn
   
    if turn == 'player':
        print ("Play")
    else:
        print ("The computer plays first")
    game_is_playing = True
    turnNumber = 0


    
    while game_is_playing:
        if turn == 'player':
            draw_board(board)
            move = Player_Move(board)
            make_move(board, player_letter, move)

            if check_winner(board, player_letter):
                draw_board(board)
                print( "You win!")
                game_is_playing = False
            if board_full(board):
                draw_board(board)
                print ("It is a tie!")
                game_is_playing = False
            else:
                turn = 'computer'

        else:
            turnNumber += 1
            move = get_move(board, computer_letter, First_Player, turnNumber, difficulty)
            make_move(board, computer_letter, move)

            if check_winner(board, computer_letter):
                draw_board(board)
                print ("The computer wins.")
                game_is_playing = False
            if board_full(board):
                draw_board(board)
                print ("Tie!")
                game_is_playing = False
            else:
                turn = 'player'

   
        #break

# In[ ]:
