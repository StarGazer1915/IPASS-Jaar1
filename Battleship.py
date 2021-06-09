# ========== STUDENT ========== #
#   Naam:       Justin Klein
#   Klas:       V1B
#   Nummer:     1707815
#   Project:    IPASS
# ============================= #


# ============ IMPORTS ============ #
from gui.Dashboard import ShowBoardGame
import random


# ============ FUNCTIONS ============ #
def createField():
    global field_size

    field = []
    for row in range(field_size):
        newrow = []
        for col in range(field_size):
            newrow.append("| |")
        field.append(newrow)

    placeShips()
    return field


def placeShips():
    global field_size
    global ship_positions
    global num_ships

    rows, cols = (field_size, field_size)
    ships_placed = 0

    ship_positions = []

    while ships_placed != num_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
        ship_size = random.randint(2, 5)
        if checkPlaceShip(random_row, random_col, direction, ship_size):
            ships_placed += 1


def showField():
    for i in createField():
        print(i)
    return


def checkValidShipPlacement(row_start, row_end, col_start, col_end):
    global battlefield
    global ship_positions

    positions_are_viable = True
    for row in range(row_start, row_end):
        for col in range(col_start,col_end):
            if battlefield[row][col] != '.':
                positions_are_viable = False
                break

    if positions_are_viable == True:
        ship_positions.append([row_start, row_end, col_start, col_end])
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                battlefield[row][col] = '0'

    return positions_are_viable


def checkPlaceShip(row, col, direction, length):
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

    return checkValidShipPlacement(row_start, row_end, col_start, col_end)


def checkShellShot():
    global row_letters
    global battlefield

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
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
            is_valid_placement = True

    return row, col


def fireShell():
    global battlefield
    global ships_destroyed
    global weapon_ammo

    row, col = checkShellShot()
    if battlefield[row][col] == ".":
        print("You missed!")
        battlefield[row][col] = "#"
    elif battlefield[row][col] == "O":
        print("You hit an enemy ship!", end=" ")
        battlefield[row][col] = "X"
        if checkShipDestroyed(row, col):
            print("A ship has been foundered!")
            ships_destroyed += 1
        else:
            print("A ship was hit!")

    weapon_ammo -= 1


def checkShipDestroyed(row, col):
    global ship_positions
    global battlefield

    for position in ship_positions:
        row_start = position[0]
        row_end = position[1]
        col_start = position[2]
        col_end = position[3]
        if row_start <= row <= row_end and col_start <= col <= col_end:
            for r in range(row_start, row_end):
                for c in range(col_start, col_end):
                    if battlefield[r][c] != "X":
                        return False
    return True


def checkGameOver():
    global ships_destroyed
    global num_ships
    global weapon_ammo
    global game_over

    if num_ships == ships_destroyed:
        print("You won the game!")
        game_over = True
    elif weapon_ammo <= 0:
        print("You ran out of bullets, the enemy has prevailed!")
        game_over = True

    return


def runGame():
    global game_over

    createField()

    while game_over is False:
        showField()
        print(f"Number of ships remaining: {str(num_ships - ships_destroyed)}\nAmmo: {str(weapon_ammo)}")
        fireShell()
        print("\n\n")
        checkGameOver()


# ============ EXECUTION ============ #
num_ships = 8
ship_positions = [[]]
ships_destroyed = 0
weapon_ammo = 50
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
battlefield = [[]]
field_size = 10
game_over = False

runGame()