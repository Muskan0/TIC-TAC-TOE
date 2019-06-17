def display(board):
    print('\n\n\n')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    m=''
    while m!='X'and m!='O':
        m= input(print("\nplayer 1: choose 'X' or 'O': \n")).upper()
    if m=='X':
        return 'X','O'
    else:
        return 'O','X'

def place_marker(board,marker,position):
    board[position]=marker

def win_check(b,m):
    return (b[1]==m and b[2]==m and b[3]==m) or (b[4]==m and b[5]==m and b[6]==m) or (b[7]==m and b[8]==m and b[9]==m) or (b[1]==m and b[4]==m and b[7]==m) or (b[5]==m and b[2]==m and b[8]==m) or (b[6]==m and b[9]==m and b[3]==m) or (b[1]==m and b[5]==m and b[9]==m) or (b[5]==m and b[7]==m and b[3]==m)

import random

def choose_First():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input(print('choose a number between(1-9)')))
    return position

def replay():
    choice= input(print('Want to play again: Enter Yes or No'))
    return choice=='Yes'
print('WELCOME TO TIC TAC TOE TWO PLAYERS GAME:\n')
while True:
    print('Note: The positions in the board are based on the numpad of a PC. ')
    myboard=[' ']*10
    p1, p2= player_input()

    turn= choose_First()
    print(turn + ' will go first')
    while True:
        if turn=='Player 1':
            display(myboard)
            print("\nPlayer 1: Your turn")
            position=player_choice(myboard)
            place_marker(myboard,p1,position)
            if win_check(myboard,p1):
                display(myboard)
                print('\nCONGRATULATIONS PLAYER 1 YOU WON THE MATCH!')
                break
            else:
                if full_board_check(myboard):
                    display(myboard)
                    print("THIS GAME IS A TIE.NOBODY WON IT.")
                    break
                else:
                    turn='Player 2'

        else:
                display(myboard)
                print("\nPlayer 2: Your turn")
                position = player_choice(myboard)
                place_marker(myboard, p2, position)
                if win_check(myboard, p2):
                    display(myboard)
                    print('\nCONGRATULATIONS PLAYER 2 YOU WON THE MATCH!')
                    break
                else:
                    if full_board_check(myboard):
                        display(myboard)
                        print("THIS GAME IS A TIE.NOBODY WON IT.")
                        break
                    else:
                        turn = 'Player 1'

    if not replay():
        break

