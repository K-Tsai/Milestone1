from IPython.display import clear_output
import random

def display_board(board):
    print(" "+ board[1] + " |" + " "+ board[2] + " |" + " "+ board[3])
    print("---" + " ---" + " ---")
    print(" "+ board[4] + " |" + " "+ board[5] + " |" + " "+ board[6])
    print("---" + " ---" + " ---")
    print(" "+ board[7] + " |" + " "+ board[8] + " |" + " "+ board[9])

def player_input():
    options = ['X','O']
    choice = "false"
    while choice not in options: 
        choice = input("Please pick a marker 'X' or 'O': ")
        if choice not in options:
            clear_output()
            print("sorry, please choose correctly. Enter 'X' or 'O'.")
            
    return choice     

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
     if board[1] == board[2] == board[3] == mark or \
        board[4] == board[5] == board[6] == mark or \
        board[7] == board[8] == board[9] == mark or \
        board[1] == board[4] == board[7] == mark or \
        board[2] == board[5] == board[8] == mark or \
        board[3] == board[6] == board[9] == mark or \
        board[1] == board[5] == board[9] == mark or \
        board[3] == board[5] == board[7] == mark:
            print(mark + " wins")

def choose_first():
    if random.randint(1, 2) == 1:
        return "Player 1 goes first"
    else: 
        return "Player 2 goes first"

def space_check(board, position):
    if board[position] == ' ':
        return False 
    else: 
        return True

def full_board_check(board):
    if board[0] == ' ' or board[1] == ' ' or board[2] == ' ' or board[3] == ' ' or \
    board[4] == ' ' or board[5] == ' ' or board[6] == ' ' or board[7] == ' ' or \
    board[8] == ' ' or board[9] == ' ':
        return False
    else:
        return True

def player_choice(board):
    options = ['0','1','2','3','4','5','6','7','8','9']
    choice = 'wrong'
    
    while choice not in options:
        
        choice = input("Choose a position from 0 to 9: ")
        
        if choice not in options:
            clear_output()
            
            print("Sorry, but you did not choose a value in the correct range of 0-9")
    integer = int(choice)
    check = space_check(board, integer)
    if check == False:
        return integer

def replay():
    options = ['yes', 'no']
    choice = 'wrong'
    
    while choice not in options:
        
        choice = input("Choose yes or no if you want to play again: ")
        
        if choice not in options:
            clear_output()
            
            print("Sorry, but you did not choose yes or no")
    if choice == 'yes':
        return True
    else:
        return False

def full_game():
  print('Welcome to Tic Tac Toe!')
  game_on= True
  game_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']
  while game_on:
    clear_output()
    display_board(game_list)
    player_input() = player_input
    player_choice = player_choice(game_list)
    place_marker(game_list, player_input, player_choice)
    clear_output()
    display_board(game_list)

full_game()