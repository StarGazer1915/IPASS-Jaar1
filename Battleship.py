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


def checkValidShipPlacement(start_row, end_row, start_col, end_col):
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