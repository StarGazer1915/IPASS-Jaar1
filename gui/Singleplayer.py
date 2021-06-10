# ============ IMPORTS ============ #
from tkinter import *
from gui.Grid import ShowFieldWindow
import random
import json

# ============ Global Variables ============ #
with open('gui/game.json', 'r') as file:
    data = json.load(file)
    try:
        field_size = data['field_size']
        amount_of_ships = data['amount_of_ships']
        ammo = data['ammo']
    except:
        field_size = 10
        amount_of_ships = 4
        ammo = 50
    file.close()

ship_min_size = 3
ship_max_size = 5
battlefield = [[]]
ship_positions = [[]]
ships_foundered = 0
game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ========================================== #

class ShowSingleplayer:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

    def __init__(self):
        self.showSingleplayer()

    def showSingleplayer(self):
        self.singleboard = Tk()
        self.singleboard.title("Battleship - Singleplayer Board")
        self.singleboard.geometry("850x600")
        self.singleboard.configure(background=self.bg)
        self.singleboard.resizable(0, 0)

        self.label1 = Label(self.singleboard, text="Singleplayer", font=("Arial 40 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.whiteline = Label(self.singleboard, font=("Arial 10 bold"))
        self.whiteline.configure(background=self.bg, foreground=self.fg)
        self.whiteline.pack()

        self.button = Button(self.singleboard, text="Show Battlefield", font=("Arial bold", 14))
        self.button.configure(height="2", width="18", command=ShowFieldWindow, highlightbackground=self.bg,foreground=self.bg)
        self.button.pack()

        self.whiteline2 = Label(self.singleboard, font=("Arial 10 bold"))
        self.whiteline2.configure(background=self.bg, foreground=self.fg)
        self.whiteline2.pack()

        self.label2 = Label(self.singleboard, text="Choose a coordinate:", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.FireEntry = Entry(self.singleboard, font=("Arial bold", 16))
        self.FireEntry.configure(highlightbackground=self.bg)
        self.FireEntry.pack()

        self.whiteline3 = Label(self.singleboard, font=("Arial bold", 10))
        self.whiteline3.configure(background=self.bg, foreground=self.fg)
        self.whiteline3.pack()

        self.FireButton = Button(self.singleboard, text="Fire!", font=("Arial bold", 14))
        self.FireButton.configure(height="2", width="8", command=self.fireShot, highlightbackground=self.bg, foreground=self.bg)
        self.FireButton.pack()

        self.whiteline4 = Label(self.singleboard, font=("Arial 10 bold"))
        self.whiteline4.configure(background=self.bg, foreground=self.fg)
        self.whiteline4.pack()

        self.label2 = Label(self.singleboard, text="====== Result: ======", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.textdash = Text(self.singleboard, font=("Arial", 16))
        self.textdash.config(height="16", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()

        self.createField()

        self.singleboard.mainloop()


    def createField(self):
        global battlefield
        global field_size
        global amount_of_ships
        global ship_positions
        global ship_min_size
        global ship_max_size

        rows, cols = field_size, field_size

        battlefield = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("_")
            battlefield.append(row)

        ships_deployed, ship_positions = 0, []

        while ships_deployed != amount_of_ships:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(0, cols - 1)
            direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
            ship_size = random.randint(ship_min_size, ship_max_size)
            if self.checkPlaceOnGrid(random_row, random_col, direction, ship_size):
                ships_deployed += 1

        return battlefield


    def checkFieldPlaceShip(self, row_start, row_end, start_col, end_col):
        global battlefield
        global ship_positions

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
                    battlefield[r][c] = "0"

        return positions_are_valid


    def checkPlaceOnGrid(self, row, col, direction, length):
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

        return self.checkFieldPlaceShip(row_start, row_end, col_start, col_end)


    def checkShellShot(self, shot):
        global row_letters
        global battlefield

        row, col = shot[0], shot[1:]
        row, col = row_letters.find(row), int(col)

        if not (-1 < col < field_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
        elif battlefield[row][col] == "#" or battlefield[row][col] == "X":
            print("You have already shot a bullet here!")

        return row, col


    def fireSequence(self, shot):
        global battlefield
        global ships_foundered
        global ammo

        self.textdash.configure(state=NORMAL)
        row, col = self.checkShellShot(shot)

        if battlefield[row][col] == "_":
            self.textdash.insert(END, f"You didn't hit anything, try again!\n\n")
            battlefield[row][col] = "#"
        elif battlefield[row][col] == "0":
            self.textdash.insert(END, f"You hit a ship!\n\n")
            battlefield[row][col] = "X"
            if self.checkShipFoundered(row, col):
                self.textdash.insert(END, f"A ship was foundered!\n\n")
                ships_foundered += 1

        self.textdash.configure(state=DISABLED)

        ammo -= 1


    def checkShipFoundered(self, row, col):
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


    def checkIfGameOver(self):
        global ships_foundered
        global amount_of_ships
        global ammo
        global game_over

        if amount_of_ships == ships_foundered:
            print("You won the game!")
            game_over = True
        elif ammo <= 0:
            print("You lost! You ran out of bullets before you could sink all the enemy ships!")
            game_over = True


    def fireShot(self):
        global row_letters

        self.textdash.configure(state=NORMAL)
        self.textdash.delete('1.0', END)

        shot = self.FireEntry.get().upper()

        if shot != '':
            if str(shot[0]) not in row_letters or str(shot[1]) in row_letters or len(shot) > 3 or len(shot) <= 1:
                self.textdash.insert(END, "That is not a valid coordinate, try again!")
            else:
                self.fireSequence(shot)
                self.insertText()
        else:
            self.textdash.insert(END, "That is not a valid coordinate, try again!")

        self.textdash.configure(state=DISABLED)
        return


    def insertText(self):
        global ammo

        self.textdash.configure(state=NORMAL)

        for i in battlefield:
            self.textdash.insert(END, f"{i}\n")

        self.textdash.insert(END, f"\nYou've got {ammo} rounds left!")

        self.textdash.configure(state=DISABLED)

        with open('gui/game.json', 'r+') as file:
            data = json.load(file)
            newgrid = {'battlefield' : battlefield}
            data.update(newgrid)
            file.seek(0)
            json.dump(data, file)
            file.close()