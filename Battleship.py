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

    return field


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
            if battlefield[row][col] != '| |':
                positions_are_viable = False
                break

    if positions_are_viable == True:
        ship_positions.append([row_start, row_end, col_start, col_end])
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                battlefield[row][col] = 'S'

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


def checkShellShot():
    pass


def fireShell():
    pass


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
    pass


def runGame():
    """
    This function runs the game.
    """
    showField()
    #ShowBoardGame()
    pass


# ============ EXECUTION ============ #
num_ships = 8
ship_positions = [[]]
ships_destroyed = 0
weapon_ammo = 50
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
battlefield = [[]]
field_size = 10

runGame()