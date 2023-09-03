from random import randrange

#define rows/columns in board
row_1 = [1, 2, 3]
row_2 = [4, 5, 6]
row_3 = [7, 8, 9]
board = [row_1, row_2, row_3]

game_on = True

available_spots = []

#function to draw the board
def check_if_winner(repeat=False, re_start='Maybe', end_game = False):
    winner = ''
    tie = False
    game_over = False
    global game_on
    # horizontal 3 in a rows
    if end_game:
        game_on = False
        return
    elif repeat == False:
        if board[0][0] == board [0][1] == board [0][2]:
            winner = board[0][0] 
            game_over = True
        elif board[1][0] == board [1][1] == board [1][2]:
            winner = board[1][0] 
            game_over = True
        elif board[2][0] == board [2][1] == board [2][2]:
            winner = board[2][0] 
            game_over = True
        #vertical three in a rows
        elif board[0][0] == board [1][0] == board [2][0]:
            winner = board[0][0] 
            game_over = True
        elif board[0][1] == board [1][1] == board [2][1]:
            winner = board[0][1] 
            game_over = True
        elif board[0][2] == board [1][2] == board [2][2]:
            game_over = True
            winner = board[0][2] 
        #diagonal three in a rows
        elif board[0][0] == board [1][1] == board [2][2]:
            winner = board[0][1] 
            game_over = True
        elif board[0][2] == board [1][1] == board [2][0]:
            winner = board[0][2] 
            game_over = True
        elif len(available_spots) == 0:
            winner = ''
            tie = True
        else:
            return
    
    
        if game_over or tie:
            print("Game Over!")
            game_on = False
            #print winner / tie message
            if game_over and winner == "X":
                print("I win!! Muahahah, try again!")
            elif game_over and winner == "O":
                print("Awwwww, lets go again! I can do better.")
            elif tie:
                print("What, a tie!? Thats no fun, boooooooooo. Lets go one more time.")
            #ask user if they want to restart
            restart = input(print("Would you like to play again? Enter 'Yes' or 'No"))
            #check to see if restart input is valid
            if restart == 'Yes' or restart == 'No':
                #if yes call this function recursively to ask for new input
                check_if_winner(repeat=True, re_start = restart)
            else:
                print("Sorry I didnt get that. You entered: ", restart, " but I only understand 'Yes' or 'No")
            
    elif repeat:
        if re_start == 'Yes':
            game_on = True
            global row_1
            global row_2
            global row_3
            row_1 = [1, 2, 3]
            row_2 = [4, 5, 6]
            row_3 = [7, 8, 9]
            play_game()
        elif re_start == 'No':
            print('Sorry to see you go! Come back again and play soon :)')
            game_on = False
            check_if_winner(end_game = True)
            return;
        else:
            print('error w repeat, value for re_start is:', restart)
    else:
        return
def draw_board():

    #iterate through each row, adding in values from each row space
    for row in board:
        print("+-------+-------+-------+\n"\
            + "|       |       |       |\n"\
            + "|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |\n"\
            + "|       |       |       |")
    print("+-------+-------+-------+")



def update_board(user, number):
    markers = ["X", "O"]
    marker = ""
    
    #set the marker to X or O depending on whether its computer or user
    if user == "computer":
        marker = markers[0]
    else:
        marker = markers[1]
    
    #search through the spaces on the board for one that matches the number parameter
    for row in board:
        for space in row:
            if space == number:
                row_index = board.index(row)
                space_index = row.index(space)
                board[row_index][space_index] = marker
                
                
    draw_board()
    check_if_winner()
    
    if game_on:
        if user == "computer":
            user_turn()
        elif user == "user":
            computer_turn()
    else:
        return
        

def update_avail_spots(restart=False):
    need_to_clear = True
    global available_spots
    
    while need_to_clear:
        for spot in available_spots:
            index = available_spots.index(spot)
            del available_spots[index]
        if len(available_spots) == 0:
            need_to_clear = False
        
    for rows in board:
        for space in rows:
            if space == "X":
                continue
            elif space == "O":
                continue
            elif space not in available_spots:
                available_spots.append(space)
            else:
                    continue
    if restart:
        for row in board:
            for space in row:
                available_spots.append(space)
        restart = False
    else:
        return
    
def user_turn(repeat=False):
    if game_on:
        if repeat:
            spot_number = int(input("Where would you like to go? Please enter an available spot #:"))
            if spot_number not in available_spots:
                print("You entered", spot_number, "which is not available. Sorry for the continued issues. Here are the available spots to choose from:", available_spots, ". Please try again!")
                user_turn(repeat=True)
            elif spot_number in available_spots:
                update_board("user", spot_number)
            else:
                print('error with input, again, at spot#:', spot_number)
                user_turn(repeat=True)
                return

        
        else:
            update_avail_spots()
            check_if_winner()
            spot_number = int(input("Where would you like to go? Please enter an available spot #:"))
    
            if spot_number not in available_spots:
                print("You entered", spot_number, "which is not available. Here are the available spots to choose from: ", available_spots, ". Please try again!")
                user_turn(repeat=True)
            elif spot_number in available_spots:
                update_board("user", spot_number)
            else:
                print("error with input:", spot_number)
                user_turn(repeat=True)
                return
    else:
        return

def computer_turn():
    update_avail_spots() 
    if game_on:  
        check_if_winner()     
        spot_number = available_spots[randrange(len(available_spots))]
        print("My turn.. I'll go here! Spot #:", spot_number)
        update_board("computer", spot_number)
    else:
        return

        
        
    
    
def play_game():
    if game_on == False:
        return
    global board
    global available_spots
    need_to_clear = True
    
    while need_to_clear:
        for spot in available_spots:
            index = available_spots.index(spot)
            del available_spots[index]
        if len(available_spots) == 0:
            need_to_clear = False
    
    board = [row_1, row_2, row_3]
    update_avail_spots(True)
    
    print("Hello! Welcome to my Python Tic-Tac-Toe game!")
    draw_board()
    print("As the computer I will go first, playing as 'X', and you will mark your spots with 'O'")
    print("I'll make my first move now:")
    update_board("computer", 5)

if game_on:
    play_game()
    