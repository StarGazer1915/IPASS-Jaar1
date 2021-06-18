# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# This file creates and updates the grid windows for the battleship Player VS AI mod.
# They can be opened by using the button (Show battlefield) in the Player VS AI window.

# ============ IMPORTS ============ #
from tkinter import *
import json
# ================================= #


class ShowAIFieldWindows:
    bg, fg = "#0033cc", "#ffffff"
    sea, hit, player_boat = '#003399', '#ff0000', '#00cc00'

    def __init__(self):
        """
        Runs the self.showPlayerField() function when the class is called.
        @return: void
        """
        self.showPlayerField()

    def showPlayerField(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the player field window when called. It uses
        the createPlayerField() function to place labels on a grid in the window and form the
        battlefield. The PlayerUpdate() function recreates/refreshes the labels in the window.
        It also calls the showAIField() function which simultaneously opens the field of the AI.

        @return: void
        """
        self.PL_FIELDBOARD = Tk()
        self.PL_FIELDBOARD.title("Battleship - Player Field")
        self.PL_FIELDBOARD.configure(background=self.bg)
        self.PL_FIELDBOARD.resizable(0, 0)

        self.createPlayerField()
        self.PlayerUpdate()
        self.showAIField()

        self.PL_FIELDBOARD.mainloop()


    def showAIField(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the AI field window when called. It uses
        the createAIField() function to place labels on a grid in the window and form the
        battlefield. The AIUpdate() function recreates/refreshes the labels in the window.

        @return: void
        """
        self.AI_FIELDBOARD = Tk()
        self.AI_FIELDBOARD.title("Battleship - AI Field")
        self.AI_FIELDBOARD.configure(background=self.bg)
        self.AI_FIELDBOARD.resizable(0, 0)

        self.createAIField()
        self.AIUpdate()

        self.AI_FIELDBOARD.mainloop()


    def createPlayerField(self):
        """
        Fills the field window with labels and places them in a grid pattern. Based on
        the battlefield of the player that it gets from the JSON file it colors specific
        labels and shows where shots from the AI hit and where they missed.
        (Blue = Sea/Missed, Red = Hit)

        It also shows the current player ship locations by coloring them green for the player.

        @return: void
        """
        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield_pl']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        battlefield = []

        pl_counter = 0
        for line in field:
            tmp_row = [Label(self.PL_FIELDBOARD, text=f"{alphabet[pl_counter]}", font=("Arial", 10),
                             height="2", width="5", background=self.bg, foreground=self.fg)]
            for char in line:
                if char == '0':
                    tmp_row.append(Label(self.PL_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.player_boat, foreground=self.bg))
                elif char == '#':
                    tmp_row.append(Label(self.PL_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.sea, foreground=self.bg))
                elif char == 'X':
                    tmp_row.append(Label(self.PL_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.hit, foreground=self.bg))
                else:
                    tmp_row.append(Label(self.PL_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, foreground=self.bg))

            battlefield.append(tmp_row)
            pl_counter += 1

        tmp_row = [Label(self.PL_FIELDBOARD, text=f"", font=("Arial", 10), height="2", width="5",
                         background=self.bg, foreground=self.fg)]

        for item in range(0, field_size):
            tmp_row.append(Label(self.PL_FIELDBOARD, text=f"{item}", font=("Arial", 10), height="2",
                                 width="5", background=self.bg, foreground=self.fg))

        battlefield.append(tmp_row)

        row = 0
        for line in battlefield:
            col = 0
            for item in line:
                item.grid(row=row, column=col, sticky=W)
                col += 1
            row += 1


    def createAIField(self):
        """
        Fills the field window with labels and places them in a grid pattern. Based on
        the battlefield of the AI that it gets from the JSON file it colors specific
        labels and shows where shots from the player hit and where they missed.
        (Blue = Sea/Missed, Red = Hit)

        @return: void
        """
        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield_ai']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        battlefield = []

        ai_counter = 0
        for line in field:
            tmp_row = [Label(self.AI_FIELDBOARD, text=f"{alphabet[ai_counter]}", font=("Arial", 10), height="2",
                             width="5", background=self.bg, foreground=self.fg)]
            for char in line:
                if char == '#':
                    tmp_row.append(Label(self.AI_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.sea, foreground=self.bg))
                elif char == 'X':
                    tmp_row.append(Label(self.AI_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, background=self.hit, foreground=self.bg))
                else:
                    tmp_row.append(Label(self.AI_FIELDBOARD, font=("Arial", 10), height="2", width="5",
                                         relief=RAISED, foreground=self.bg))

            battlefield.append(tmp_row)
            ai_counter += 1

        tmp_row = [Label(self.AI_FIELDBOARD, text=f"", font=("Arial", 10), height="2", width="5",
                         background=self.bg, foreground=self.fg)]

        for item in range(0, field_size):
            tmp_row.append(Label(self.AI_FIELDBOARD, text=f"{item}", font=("Arial", 10), height="2",
                                 width="5", background=self.bg, foreground=self.fg))

        battlefield.append(tmp_row)

        row = 0
        for line in battlefield:
            col = 0
            for item in line:
                item.grid(row=row, column=col, sticky=W)
                col += 1
            row += 1


    def PlayerUpdate(self):
        """
        Calls the createPlayerField() function every 5 seconds to update
        the field and show where shots from the AI landed.
        @return: void
        """
        self.createPlayerField()
        self.PL_FIELDBOARD.after(5000, self.PlayerUpdate)


    def AIUpdate(self):
        """
        Calls the createAIField() function every 5 seconds to update
        the field and show where shots from the player landed.
        @return: void
        """
        self.createAIField()
        self.AI_FIELDBOARD.after(5000, self.AIUpdate)
