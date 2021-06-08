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
    global field_size

    field = []
    for row in range(field_size):
        newrow = []
        for col in range(field_size):
            newrow.append("O")
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
            if battlefield[row][col] != '0':
                positions_are_viable = False
                break

    if positions_are_viable == True:
        ship_positions.append([row_start, row_end, col_start, col_end])
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                battlefield[row][col] = 'S'

    return positions_are_viable


def placeShip(row, col, direction, length):
    global field_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1

    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= field_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= field_size:
            return False
        end_row = row + length


    pass


def checkShellChoice():
    pass


def fireShell():
    pass


def checkShipDestroyed(row, col):
    pass


def checkGameOver():
    pass


def runGame():
    """
    This function runs the game.
    """
    showField()
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