# CS-UY 1114
# Final project
# Indra Ratna
# EXL3
# Epstein
import math
import turtle
import time
import random

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def get_coordinates(s):
    """
    sig: int -> tuple
    based on the index of the_board which has been
    filled by the user or computer, coordinates are
    returned to draw the symbol of the move onto the
    turtle board
    """
    x=-40
    y=120
    if(s<3):
        y=120
    elif(s<6):
        y=40
    elif(s<9):
        y=-40
    x=x+(80*((s)%3))
    return(x,y)


def draw_x(x,y):
    """
    signature: tuple -> NoneType
    Given the a set of coordinates for
    a square of the tic-tac-toe board,
    an X is drawn on the board to
    signify a computer move.
    """
    turtle.setheading(0)
    turtle.color("red")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.left(45)
    turtle.forward(math.sqrt(12800))
    turtle.up()
    turtle.goto(x,y+80)
    turtle.down()
    turtle.right(90)
    turtle.forward(math.sqrt(12800))

def draw_circle(x,y):
    """
    signature: tuple -> NoneType
    Given the a set of coordinates from
    the user click, a set of coordinates
    is given for the square clicked on
    the board. The circle then represents
    a user move on the board.
    """
    turtle.setheading(0)
    turtle.color('green')
    turtle.up()
    turtle.goto(x+40,y)
    turtle.down()
    turtle.circle(40)
    
def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    turtle.setheading(0)
    turtle.color("black")
    turtle.up()
    turtle.goto(-40,-40)
    turtle.down()
    for i in range(4):
        turtle.forward(240)
        turtle.left(90)
    turtle.left(90)
    for i in range (-40,240,80):
        turtle.up()
        turtle.goto(i,-40)
        turtle.down()
        turtle.forward(240)
    turtle.right(90)
    for i in range (-40,240,80):
        turtle.up()
        turtle.goto(-40,i)
        turtle.down()
        turtle.forward(240)
    #draws X and O on the board based on
    #updated list of the_board
    for index in range (len(board)):
        if(board[index] == "X"):
            spot = (get_coordinates(index))
            x = spot[0]
            y = spot[1]
            draw_x(x,y)
        elif(board[index]=="O"):
            spot = (get_coordinates(index))
            x = spot[0]
            y = spot[1]
            draw_circle(x,y)
    turtle.update()

def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    #looping through row by row to check if
    # given x and y coordinates fall into a box
    if(x>=-40 and x<=40):
        if(y>=-40 and y<=40):
            if(board[6]=="_"):
                board[6]="O"
                return True
        elif(y>=-140 and y<=-90):
            print("restart button clicked")
            restart_button = True
            return True
        elif(y>=40 and y<=120):
            if(board[3]=="_"):
                board[3] ="O"
                return True
        elif(y>=120 and y<=200):
            if(board[0]=="_"):
                board[0]="O"
                return True
    elif(x>=40 and x<=120):
        if(y>=-40 and y<=40):
            if(board[7]=="_"):
                board[7]="O"
                return True
        elif(y>=-140 and y<=-90):
            print("restart button clicked")
            restart_button = True
            return True
        elif(y>=40 and y<=120):
            if(board[4]=="_"):
                board[4]="O"
                return True
        elif(y>=120 and y<=200):
            if(board[1]=="_"):
                board[1]="O"
                return True
    elif(x>=120 and x<=200):
        if(y>=-40 and y<=40):
            if(board[8]=="_"):
                board[8]="O"
                return True
        elif(y>=40 and y<=120):
            if(board[5]=="_"):
                board[5]="O"
                return True
        elif(y>=120 and y<=200):
            if(board[2]=="_"):
                board[2]="O"
            return True
    return False


def message(words,color,x,y):
    """
    signature: str,str,int,int -> NoneType
    message takes a set of words and the
    color the user wants them printed in.
    Then it prints it on turtle at the
    coordinates inputted. This function
    always prints the message in Arial font
    at size 30.
    """
    turtle.color(color)
    turtle.up()
    turtle.goto(x,y)
    turtle.down
    turtle.hideturtle
    turtle.write(words,move=False,align="left",font=("Arial",30,"normal"))
    turtle.up()    

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemate, display
    an appropriate message to the user and clear the board
    in preparation for the next round. The game is restarted
    by clicking a new square if the game was won or waiting 3
    seconds after the game is ended by stalemate.
    If the game is over, return True, otherwise False.
    """
    global the_board
    the_board = board
    #checking if X has won the game
    if is_won(the_board,"X")[0] == True:
        message(is_won(the_board,"X")[1]+" has won!","red",-40,-90)
        turtle.up()
        time.sleep(3)
        the_board = [ "_", "_", "_",
                      "_", "_", "_",
                      "_", "_", "_"]
        return True
    #checking if O has won the game
    elif is_won(the_board,"O")[0] == True:
        message(is_won(the_board,"O")[1]+" has won!","green",-40,-90)
        time.sleep(3)
        the_board = [ "_", "_", "_",
                      "_", "_", "_",
                      "_", "_", "_"]
        return True
    #checking if a tie has occurred
    elif board.count("_")==0:
        message("TIE","black",-40,-90)
        time.sleep(3)
        the_board = [ "_", "_", "_",
                      "_", "_", "_",
                      "_", "_", "_"]    
        return True
    else:
        #game continues if none of the conditions are true
        return False

def is_won(board,letter):
    """
    signature: list,str -> bool,str
    is_won checks if any of the eight
    possible winning combinations have
    been acheived by either the user
    or the computer. If a combination is
    found to have won then the function
    returns True and the winning letter.
    Otherwise it returns False and still
    returns the letter checked.
    """
    #checking for horizontal win
    for i in range(0,9,3):
        if(board[i]==board[i+1]==board[i+2]==letter):
            return (True,letter)
    #checking for vertical win 
    for i in range(0,3):
        if(board[i]==board[i+3]==board[i+6]==letter):
            return (True,letter)
    #checking the first diagonal win 
    i=0
    if(board[i]==board[i+4]==board[i+8]==letter):
       return (True,letter)
    #checking the second diagonal win
    i=2
    if(board[i]==board[i+2]==board[i+4]==letter):
       return(True,letter)
    #returning that the given letter hasn't won the game  
    return (False,letter)

    
def find_cpu_index(board):
    """
    signature: list(str) -> int
    By checking empty positions of
    the board into possibleMoves,
    the function checks if any of the
    given spaces could end the game
    and places the computer move at
    that position to either block a
    user win or win for the computer.
    Otherwise, a random corner is chosen
    and if all corners are taken a random
    edge is chosen with the index of
    the_board that the move needs being
    returned.
    """
    #creating a list of possible moves
    empty_spaces =[]
    for i in range(len(board)):
        if(board[i]=="_"):
            empty_spaces.append(i)
    #checking for moves to end the game
    move = 0
    for letter in["X","O"]:
        for i in empty_spaces:
            boardCopy = board[:]
            boardCopy[i]=letter
            if is_won(boardCopy,letter)[0]:
                move = i
                the_board[move]="X"
                return move
    #checking for empty corner spaces to occupy
    cornersOpen = []
    for i in empty_spaces:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move = random.choice(cornersOpen)
        the_board[move]="X"
        return move
    if 4 in empty_spaces:
        move = 4
        the_board[move]="X"
        return move
    #randomly choosing an open edge space
    edgesOpen = []
    for i in empty_spaces:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move = random.choice(edgesOpen)
        the_board[move]="X"
    return move
    
def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
        """
    #most of this is done in helper function find_cpu_index
    move = find_cpu_index(board)
    point = get_coordinates(move)
    #taking points from the tuple returned by get_coordinates
    x = point[0]
    y = point[1]
    draw_x(x,y)


def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)
        else:
            draw_board(the_board)
        

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()
main()
