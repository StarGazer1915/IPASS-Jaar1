# ========== STUDENT ========== #
#   Naam:       Justin Klein
#   Klas:       V1B
#   Nummer:     1707815
#   Project:    IPASS
# ============================= #


# ============ IMPORTS ============ #
import random


# ============ FUNCTIONS ============ #
def createField():
    global battlefield
    global field_size
    global amount_of_ships
    global ship_positions

    rows = field_size
    cols = field_size

    battlefield = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        battlefield.append(row)

    ships_deployed = 0
    ship_positions = []

    while ships_deployed != amount_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
        ship_size = random.randint(ship_min_size, ship_max_size)
        if checkPlaceOnGrid(random_row, random_col, direction, ship_size):
            ships_deployed += 1


def showField():
    global battlefield
    for i in battlefield:
        print(i)


def checkFieldPlaceShip(row_start, row_end, start_col, end_col):
    global battlefield
    global ship_positions

    positions_are_valid = True
    for r in range(row_start, row_end):
        for c in range(start_col, end_col):
            if battlefield[r][c] != ".":
                positions_are_valid = False
                break
    if positions_are_valid == True:
        ship_positions.append([row_start, row_end, start_col, end_col])
        for r in range(row_start, row_end):
            for c in range(start_col, end_col):
                battlefield[r][c] = "O"

    return positions_are_valid


def checkPlaceOnGrid(row, col, direction, length):
    global field_size

    row_start = row
    row_end = row+1
    col_start = col
    col_end = col+1

    if direction == "LEFT":
        if col - length < 0:
            return False
        col_start = col - length + 1

    elif direction == "RIGHT":
        if col + length >= field_size:
            return False
        col_end = col + length

    elif direction == "UP":
        if row - length < 0:
            return False
        row_start = row - length + 1

    elif direction == "DOWN":
        if row + length >= field_size:
            return False
        row_end = row + length

    return checkFieldPlaceShip(row_start, row_end, col_start, col_end)


def checkShellShot():
    global row_letters
    global battlefield

    row = -1
    col = -1
    valid_shot = False
    while valid_shot is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = row_letters.find(row)
        if not (-1 < row < field_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < field_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if battlefield[row][col] == "#" or battlefield[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if battlefield[row][col] == "." or battlefield[row][col] == "O":
            valid_shot = True

    return row, col


def fireShell():
    global battlefield
    global ships_foundered
    global ammo

    row, col = checkShellShot()

    if battlefield[row][col] == ".":
        print("\nYou didn't hit anything, try again!\n")
        battlefield[row][col] = "#"
    elif battlefield[row][col] == "O":
        print("\nYou hit a ship!")
        battlefield[row][col] = "X"
        if checkShipFoundered(row, col):
            print("\nA ship was foundered!\n")
            ships_foundered += 1
        else:
            print("A ship was hit!\n")

    ammo -= 1


def checkShipFoundered(row, col):
    global ship_positions
    global battlefield

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if battlefield[r][c] != "X":
                        return False

    return True


def checkIfGameOver():
    global ships_foundered
    global amount_of_ships
    global ammo
    global game_over

    if amount_of_ships == ships_foundered:
        print("You won the game!")
        game_over = True
    elif ammo <= 0:
        print("Sorry, you lost! You ran out of bullets!")
        game_over = True


def runGame():
    global game_over

    createField()
    while game_over is False:
        showField()
        print(f"Ships remaining: {str(amount_of_ships - ships_foundered)}\nAmmo: {str(ammo)}")
        fireShell()
        checkIfGameOver()


# ============ EXECUTION ============ #
field_size = 10
amount_of_ships = 4
ship_min_size = 3
ship_max_size = 5
battlefield = [[]]
ship_positions = [[]]
ammo = 50
ships_foundered = 0
game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Used global variables because using them as parameters would be chaotic.

runGame()