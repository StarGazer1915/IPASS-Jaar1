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
    global battlefield

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

    viable_positions = True
    for row in range(row_start, row_end):
        for col in range(col_start,col_end):
            if battlefield[row][col] != '.':
                viable_positions = False
                break

    if viable_positions == True:
        ship_positions.append([row_start, row_end, col_start, col_end])
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):


    pass


def placeShip(row, col, direction, length):
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