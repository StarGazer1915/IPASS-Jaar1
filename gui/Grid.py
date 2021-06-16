# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# This file creates and updates the grid window for the battleship game.
# It can be opened by using the button (Show battlefield) in the singleplayer window.

# ============ IMPORTS ============ #
from tkinter import *
import json
# ================================= #


class ShowFieldWindow:
    bg, fg = "#0033cc", "#ffffff"
    sea, hit = '#003399', '#ff0000'

    def __init__(self):
        """
        Runs the self.showField() function when the class is called.
        @return: void
        """
        self.showField()

    def showField(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the field window when called. It uses
        the createField() function to place labels on a grid in the window and form the
        battlefield. The update() function recreates/refreshes the labels in the window.

        @return: void
        """
        self.GRIDBOARD = Tk()
        self.GRIDBOARD.title("Battleship - Field")
        self.GRIDBOARD.configure(background=self.bg)
        self.GRIDBOARD.resizable(0, 0)

        self.createField()
        self.update()

        self.GRIDBOARD.mainloop()


    def createField(self):
        """
        Fills the field window with labels and places them in a grid pattern. Based on
        the battlefield that it gets from the JSON file it colors specific labels and
        shows where shots hit and where they missed. (Blue = Sea/Missed, Red = Hit)

        @return: void
        """
        with open('gui/SingleplayerGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        battlefield = []

        # Generated (colored)labels in and store them in a list. #
        counter = 0
        for line in field:
            tmp_row = [Label(self.GRIDBOARD, text=f"{alphabet[counter]}", font=("Arial", 10),
                             height="2", width="5", background=self.bg, foreground=self.fg)]
            for char in line:
                if char == '#':
                    tmp_row.append(Label(self.GRIDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.sea, foreground=self.bg))
                elif char == 'X':
                    tmp_row.append(Label(self.GRIDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.hit, foreground=self.bg))
                else:
                    tmp_row.append(Label(self.GRIDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, foreground=self.bg))

            battlefield.append(tmp_row)
            counter += 1

        tmp_row = [Label(self.GRIDBOARD, text=f"", font=("Arial", 10), height="2", width="5",
                         background=self.bg, foreground=self.fg)]

        for item in range(0,field_size):
            tmp_row.append(Label(self.GRIDBOARD, text=f"{item}", font=("Arial", 10), height="2",
                                 width="5", background=self.bg, foreground=self.fg))

        battlefield.append(tmp_row)

        # Place the generated labels in a grid pattern. #
        row = 0
        for line in battlefield:
            col = 0
            for item in line:
                item.grid(row=tmp_row, column=col, sticky=W)
                col += 1
            row += 1


    def update(self):
        """
        Calls the createField() function every 5 seconds to update
        the field and show where shots landed.
        @return: void
        """
        self.createField()
        self.GRIDBOARD.after(5000, self.update)