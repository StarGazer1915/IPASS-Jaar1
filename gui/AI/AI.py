# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Klas:       V1B
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# ============ IMPORTS ============ #
from tkinter import *
from gui.AI.AIGrid import ShowAIFieldWindow
import random
import json

# ============ GLOBALS ============ #
field_size = 0
amount_of_ships = 0
ammo = 0

ship_min_size = 3
ship_max_size = 5

ships_foundered_pl = 0
ships_foundered_ai = 0
battlefield_pl = [[]]
battlefield_ai = [[]]
ship_positions_pl = [[]]
ship_positions_ai = [[]]

game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ================================= #


class ShowAIGame:
    # ======== Visuals ======== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

    def __init__(self):
        global game_over
        game_over = False

        global ships_foundered_pl
        global ships_foundered_ai
        ships_foundered_pl = 0
        ships_foundered_ai = 0

        self.loadJson()
        self.showSingleplayer()


    def showSingleplayer(self):
        self.aiboard = Tk()
        self.aiboard.title("Battleship - AI Game Board")
        self.aiboard.geometry("850x600")
        self.aiboard.configure(background=self.bg)
        self.aiboard.resizable(0, 0)

        self.label1 = Label(self.aiboard, text="AI Game", font=("Arial 40 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.whiteline = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline.configure(background=self.bg, foreground=self.fg)
        self.whiteline.pack()

        self.button = Button(self.aiboard, text="Show Battlefield", font=("Arial bold", 14))
        self.button.configure(height="2", width="18", command=ShowAIFieldWindow, highlightbackground=self.bg,foreground=self.bg)
        self.button.pack()

        self.whiteline2 = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline2.configure(background=self.bg, foreground=self.fg)
        self.whiteline2.pack()

        self.label2 = Label(self.aiboard, text="Choose a coordinate:", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.FireEntry = Entry(self.aiboard, font=("Arial bold", 16))
        self.FireEntry.configure(highlightbackground=self.bg)
        self.FireEntry.pack()

        self.whiteline3 = Label(self.aiboard, font=("Arial bold", 10))
        self.whiteline3.configure(background=self.bg, foreground=self.fg)
        self.whiteline3.pack()

        self.FireButton = Button(self.aiboard, text="Fire!", font=("Arial bold", 14))
        self.FireButton.configure(height="2", width="8", command=self.fireShot, highlightbackground=self.bg, foreground=self.bg)
        self.FireButton.pack()

        self.whiteline4 = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline4.configure(background=self.bg, foreground=self.fg)
        self.whiteline4.pack()

        self.label2 = Label(self.aiboard, text="====== Result: ======", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.textdash = Text(self.aiboard, font=("Arial", 16))
        self.textdash.config(height="16", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()

        self.createFields()
        self.jsonBattlefield({'battlefield_pl': battlefield_pl})
        self.jsonBattlefield({'battlefield_ai': battlefield_ai})

        self.aiboard.mainloop()


    def makeField(self, battlefield, rows, cols):
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("_")
            battlefield.append(row)

        return battlefield


    def makeShipPositions(self, ship_positions, amount_of_ships, rows, cols):
        ships_deployed, ship_positions = 0, []

        while ships_deployed != amount_of_ships:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(0, cols - 1)
            direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
            ship_size = random.randint(ship_min_size, ship_max_size)
            if self.checkPlaceOnGrid(random_row, random_col, direction, ship_size):
                ships_deployed += 1

        return ship_positions


    def createFields(self):
        global field_size
        global amount_of_ships
        global ship_min_size
        global ship_max_size
        global battlefield_pl
        global battlefield_ai
        global ship_positions_pl
        global ship_positions_ai

        rows, cols = field_size, field_size
        battlefield_pl, battlefield_ai = [], []

        battlefield_pl = self.makeField(battlefield_pl, rows, cols)
        battlefield_ai = self.makeField(battlefield_ai, rows, cols)
        ship_positions_pl = self.makeShipPositions(ship_positions_pl, amount_of_ships, rows, cols)
        ship_positions_ai = self.makeShipPositions(ship_positions_ai, amount_of_ships, rows, cols)


    def checkFieldPlaceShip(self, battlefield, ship_positions, row_start, row_end, start_col, end_col):
        positions_are_valid = True
        for r in range(row_start, row_end):
            for c in range(start_col, end_col):
                if battlefield[r][c] != "_":
                    positions_are_valid = False
                    break

        if positions_are_valid == True:
            ship_positions.append([row_start, row_end, start_col, end_col])
            for r in range(row_start, row_end):
                for c in range(start_col, end_col):
                    battlefield_pl[r][c] = "0"

        return [battlefield, ship_positions]


    def checkPlaceOnGrid(self, battlefield, ship_positions, row, col, direction, length):
        global field_size

        row_start, row_end, col_start, col_end = row, row+1, col, col+1

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

        return self.checkFieldPlaceShip(battlefield, ship_positions, row_start, row_end, col_start, col_end)


    def checkShellShot(self, shot):
        global row_letters
        global battlefield_pl

        row, col = shot[0], shot[1:]
        row, col = row_letters.find(row), int(col)

        if battlefield_pl[row][col] == "#" or battlefield_pl[row][col] == "X":
            self.textdash.configure(state=NORMAL)
            self.textdash.insert(END, f"You have already fired a shell here!\n\n")
            self.textdash.configure(state=DISABLED)

        return row, col


    def fireSequence(self, shot):
        global battlefield_pl
        global ships_foundered_pl
        global ammo

        self.textdash.configure(state=NORMAL)
        row, col = self.checkShellShot(shot)

        if battlefield_pl[row][col] == "_":
            self.textdash.insert(END, f"You didn't hit anything, try again!\n\n")
            battlefield_pl[row][col] = "#"
        elif battlefield_pl[row][col] == "0":
            self.textdash.insert(END, f"You hit a ship!\n")
            battlefield_pl[row][col] = "X"
            if self.checkShipFoundered(row, col):
                self.textdash.insert(END, f"A ship was foundered!\n\n")
                ships_foundered_pl += 1

        self.textdash.configure(state=DISABLED)
        ammo -= 1


    def checkShipFoundered(self, row, col):
        global ship_positions_pl
        global battlefield_pl

        for position in ship_positions_pl:
            start_row = position[0]
            end_row = position[1]
            start_col = position[2]
            end_col = position[3]
            if start_row <= row <= end_row and start_col <= col <= end_col:
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        if battlefield_pl[r][c] != "X":
                            return False

        return True


    def checkIfGameOver(self):
        global ships_foundered_pl
        global amount_of_ships
        global ammo
        global game_over

        if amount_of_ships == ships_foundered_pl:
            self.textdash.configure(state=NORMAL)
            self.textdash.delete('1.0', END)
            self.textdash.insert(END, "You won the game!\nCongratulations!")
            self.textdash.configure(state=DISABLED)
            game_over = True

        elif ammo <= 0:
            self.textdash.configure(state=NORMAL)
            self.textdash.delete('1.0', END)
            self.textdash.insert(END, "You lost!\nYou ran out of bullets!")
            self.textdash.configure(state=DISABLED)
            game_over = True


    def fireShot(self):
        global row_letters

        self.textdash.configure(state=NORMAL)
        self.textdash.delete('1.0', END)

        shot = self.FireEntry.get().upper()

        if shot != '' and game_over != True:
            if str(shot[0]) not in row_letters or str(shot[1]) in row_letters or len(shot) > 3 or len(shot) <= 1:
                self.textdash.insert(END, "That is not a valid coordinate, try again!")
            else:
                self.fireSequence(shot)
                self.insertText()
                self.checkIfGameOver()
        elif game_over:
            self.textdash.insert(END, "The game has ended!\nClose the windows and play again\nfrom the main menu!")
        else:
            self.textdash.insert(END, "That is not a valid coordinate, try again!")

        self.textdash.configure(state=DISABLED)


    def insertText(self):
        global ammo

        self.textdash.configure(state=NORMAL)
        self.textdash.insert(END, f"\nYou've got {ammo} rounds left!\n\n")

        for i in battlefield_pl:
            self.textdash.insert(END, f"{i}\n")

        self.textdash.configure(state=DISABLED)
        self.jsonBattlefield({'battlefield': battlefield_pl})


    def jsonBattlefield(self, item):
        with open('gui/AI/AIGame.json', 'r+') as file:
            data = json.load(file)
            data.update(item)
            file.seek(0)
            json.dump(data, file)
            file.close()


    def loadJson(self):
        global field_size
        global amount_of_ships
        global ammo

        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            amount_of_ships = data['amount_of_ships']
            ammo = data['ammo']
            file.close()