import random
"""


"""

# To print the field
def field():
    # Transfer the numbers in cells to spaces
    cells_2 = []
    for i in cells:
        if i != "X" and i != "O":
            cells_2.append(" ")
        else:
            cells_2.append(i)
    print(f"""
    ---------
    | {cells_2[0]} {cells_2[1]} {cells_2[2]} |
    | {cells_2[3]} {cells_2[4]} {cells_2[5]} |
    | {cells_2[6]} {cells_2[7]} {cells_2[8]} |
    ---------
    """)

# Players move
def player(command):
    global cells
    while True:
        coordinates = input("Enter the coordinates: ").split()

        # Try if the user input numbers
        try:
            coordinates = [int(i) for i in coordinates]
        except ValueError:
            print("You should enter numbers!")
            continue

        # Try if are there 2 coordinates and if are they in the range 1 to 3
        if len(coordinates) != 2:
            print("Please input two coordinates")
            continue
        elif coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] < 1 or coordinates[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        # Tranfer the coordinats from 2D to 1D
        else:
            coordinates = transfer_coordinates(coordinates)

            # Try if the cell is already occupied
            if cells[coordinates] == "X" or cells[coordinates] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                if command == "X":
                    cells[coordinates] = "X"
                    break
                elif command == "O":
                    cells[coordinates] = "O"
                    break
# Computer's easy move - completely random moves
def computer_easy(command):
    global cells
    while True:
        coordinates = random.randrange(0,9)

        if cells[coordinates] == "X" or cells[coordinates] == "O":
            continue
        else:
            if command == "X":
                cells[coordinates] = "X"
                break
            elif command == "O":
                cells[coordinates] = "O"
                break

# Computer's medium move - it will stop the player to win if he can win in one move
# or win himself in one move
def computer_medium(command):
    global cells
    # Transfer the field from 1D to 2D
    cells_2 = [[cells[6], cells[7], cells[8]], [cells[3], cells[4], cells[5]], [cells[0], cells[1], cells[2]]]

    # Exchange the numbers by spaces
    for i in range(3):
        for j in range(3):
            if type(cells_2[i][j]) == int:
                cells_2[i][j] = " "

    identify = 0
    while True:
        # Check the rows
        count_command = 0
        count_command_oponent = 0
        count_space = 0
        for i in range(3):
            for j in range(3):
                if cells_2[i][j] == command:
                    count_command += 1
                elif cells_2[i][j] != command and cells_2[i][j] != " ":
                    count_command_oponent += 1

            # If in the line are two X or two O
            if count_command == 2 or count_command_oponent == 2:

                # If in the row is space, place there computers move
                if " " in cells_2[i]:
                    for j in range(3):
                        if cells_2[i][j] == " ":
                            cells[transfer_coordinates([j+1, i+1])] = command
                            identify = 1
                else:
                    count_command = 0
                    count_command_oponent = 0
                    continue
                break
            else:
                count_command = 0
                count_command_oponent = 0

        if identify == 1:
            break

        # Check the columns
        for i in range(3):
            for j in range(3):
                if cells_2[j][i] == command:
                    count_command += 1
                elif cells_2[j][i] != command and cells_2[j][i] != " ":
                    count_command_oponent += 1
                elif cells_2[j][i] == " ":
                    count_space += 1

            # If in the column are two X or two O
            if (count_command == 2 or count_command_oponent == 2) and count_space == 1:

                for j in range(3):
                    # If in the column is space, place there computers move
                    if cells_2[j][i] == " ":
                        cells[transfer_coordinates([i+1, j+1])] = command
                        identify = 1
                        break
            else:
                count_command = 0
                count_command_oponent = 0
                count_space = 0

            break

        if identify == 1:
            break
        # Check the first diagonal
        for i in range(3):
            if cells_2[i][i] == command:
                count_command += 1
            elif cells_2[i][i] != command and cells_2[i][i] != " ":
                count_command_oponent += 1
            elif cells_2[i][i] == " ":
                count_space += 1

        if (count_command == 2 or count_command_oponent == 2) and count_space == 1:

            for j in range(3):
                if cells_2[j][j] == " ":
                    cells[transfer_coordinates([j+1, j+1])] = command
                    identify = 1
                    break
        else:
            count_command = 0
            count_command_oponent = 0
            count_space = 0

        if identify == 1:
            break
        # Check the second diagonal
        j = 2
        for i in range(3):
            if cells_2[i][j] == command:
                count_command += 1
                j -= 1
            elif cells_2[i][j] != command and cells_2[i][j] != " ":
                count_command_oponent += 1
                j -= 1
            elif cells_2[i][j] == " ":
                count_space += 1
                j -= 1

        if (count_command == 2 or count_command_oponent == 2) and count_space == 1:
            j = 2
            for i in range(3):
                if cells_2[i][j] == " ":
                    cells[transfer_coordinates([j+1, i+1])] = command
                    identify = 1
                    break
                else:
                    j -= 1
        else:
            count_comand = 0
            count_comand_oponent = 0
            count_space = 0


        # If the game can not finnish in one move, play random move
        if identify == 0:
            computer_easy(command)
            break
        else:
            break

# Coputer's hard move - recursive check for all available places and chose the perfect one
def computer_hard(newBoard, player):
    global fc, cells
    fc += 1

    #available spots
    availSpots = empty_indexies(newBoard)

    # Check for the terminal states as win, lose, and draw and returning a proper value
    if winning(newBoard,hu_player) == True:
        return {"score":-10}
    elif winning(newBoard, ai_player) == True:
        return {"score":10}
    elif len(availSpots) == 0:
        return {"score":0}

    # An array to collect all the objects
    moves = []

    # Loop throuh available spots
    for i in availSpots:
        # Create an object for each and store the index of that sport that e´was stored as a number
        # in the object's index key
        move = {}
        move["index"] = newBoard[i]

        # Set the empty spot to the current player
        newBoard[i] = player

        # id collect the score resulted from calling computer_hard on the opponent of the current player
        if player == ai_player:
            result = computer_hard(newBoard, hu_player)
            move["score"] = result["score"]

        else:
            result = computer_hard(newBoard, ai_player)
            move["score"] = result["score"]

        # reset the sport to empty
        newBoard[i] = move["index"]

        # push the object to the arry
        moves.append(move)

    # If it is the computer's move turn loop over the moves and choose the move with the highest score
    best_move = 0
    if player == ai_player:
        best_score = -10000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i
    # else loop over the moves and choose the move with lowest score
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i

    # Return the chosen move from array to the higher depth
    return moves[best_move]

# Return the available spots on the board
def empty_indexies(board):
    empty_board = []
    for i in board:
        if i != "O" and i != "X":
            empty_board.append(i)
    return empty_board

# Transfer the coordinates from 2D to 1D
def transfer_coordinates(coordinates):
    if coordinates == [1, 1]:
        return 6
    elif coordinates == [1, 2]:
        return 3
    elif coordinates == [1, 3]:
        return 0
    elif coordinates == [2, 1]:
        return 7
    elif coordinates == [2, 2]:
        return 4
    elif coordinates == [2, 3]:
        return 1
    elif coordinates == [3, 1]:
        return 8
    elif coordinates == [3, 2]:
        return 5
    elif coordinates == [3, 3]:
        return 2

# Winning combinations
def winning(cells, player):


    count_spaces = 0
    for i in cells:
        if type(i) == int:
            count_spaces += 1

    if (cells[0] == player and cells[1] == player and cells[2] == player or
        cells[3] == player and cells[4] == player and cells[5] == player or
        cells[6] == player and cells[7] == player and cells[8] == player or
        cells[0] == player and cells[3] == player and cells[6] == player or
        cells[1] == player and cells[4] == player and cells[7] == player or
        cells[2] == player and cells[5] == player and cells[8] == player or
        cells[0] == player and cells[4] == player and cells[8] == player or
        cells[2] == player and cells[4] == player and cells[6] == player):
        return True
    elif count_spaces == 0:
        return "draw"
    else:
        return False

# Reset the field to the start statement
def new_cells():
    global cells
    cells = [0,1,2,3,4,5,6,7,8]
    pass




cells = [0,1,2,3,4,5,6,7,8]

# Start the game
while True:

    command = input("Input command: ").split()
    if command[0] == "exit":
        break
    elif len(command) == 1 or len(command) == 2:
        print("Bad parameters!")
    elif len(command) == 3:
        while True:
            # Player 1
            if command[1] == "user":
                player("X")
            elif command[1] == "easy":
                print("Making move level easy")
                computer_easy("X")
            elif command[1] == "medium":
                print("Making move level medium")
                computer_medium("X")
            elif command[1] == "hard":
                print("making move level hard")
                hu_player = "O"
                ai_player = "X"
                fc = 0
                cells[computer_hard(cells,"X")["index"]] = "X"
            else:
                print("Bad parameters")
                break
            field()


            if winning(cells, "X") == True:
                print("X wins")
                new_cells()
                break
            elif winning(cells, "X") == "draw":
                print("draw")
                new_cells()
                break


            # Player 2
            if command[2] == "user":
                player("O")
            elif command[2] == "easy":
                print("Making move level easy")
                computer_easy("O")
            elif command[2] == "medium":
                print("Making move level medium")
                computer_medium("O")
            elif command[2] == "hard":
                print("making move level hard")
                hu_player = "X"
                ai_player = "O"
                fc = 0
                cells[computer_hard(cells,"O")["index"]] = "O"
            else:
                print("Bad parameters")
                break
            field()

            if winning(cells, "O") == True:
                print("O wins")
                new_cells()
                break
            elif winning(cells, "O") == "draw":
                print("draw")
                new_cells()
                break

