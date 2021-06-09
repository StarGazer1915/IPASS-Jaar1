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


def placeShip():
    pass

def checkShellShot():
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