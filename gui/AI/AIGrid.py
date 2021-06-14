# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Klas:       V1B
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# ============ IMPORTS ============ #
from tkinter import *
import json
# ================================= #


class ShowAIFieldWindows:
    # ======== Visuals ======== #
    bg, fg = "#0033cc", "#ffffff"
    sea, hit, player_boat = '#003399', '#ff0000', '#00cc00'
    # ========================= #

    def __init__(self):
        self.showPlayerField()

    def showPlayerField(self):
        self.fieldboard = Tk()
        self.fieldboard.title("Battleship - Player Field")
        self.fieldboard.configure(background=self.bg)
        self.fieldboard.resizable(0,0)

        self.createPlayerField()
        self.showAIField()

        #self.update()

        self.fieldboard.mainloop()


    def showAIField(self):
        self.aifieldboard = Tk()
        self.aifieldboard.title("Battleship - AI Field")
        self.aifieldboard.configure(background=self.bg)
        self.aifieldboard.resizable(0,0)

        self.createAIField()
        #self.update()

        self.aifieldboard.mainloop()


    def createPlayerField(self):
        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield_pl']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        battlefield = []
        i = 0
        for r in field:
            row = []
            row.append(Label(self.fieldboard, text=f"{alphabet[i]}", font=("Arial", 10), height="2",
                             width="5", background=self.bg, foreground=self.fg))

            for char in r:
                if char == '0':
                    row.append(Label(self.fieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, background=self.player_boat, foreground=self.bg))
                elif char == '#':
                    row.append(Label(self.fieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, background=self.sea, foreground=self.bg))
                elif char == 'X':
                    row.append(Label(self.fieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, background=self.hit, foreground=self.bg))
                else:
                    row.append(Label(self.fieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, foreground=self.bg))

            battlefield.append(row)
            i += 1

        row = []
        row.append(Label(self.fieldboard, text=f"", font=("Arial", 10), height="2", width="5",
                         background=self.bg, foreground=self.fg))

        for item in range(0,field_size):
            row.append(Label(self.fieldboard, text=f"{item}", font=("Arial", 10), height="2", width="5",
                             background=self.bg, foreground=self.fg))

        battlefield.append(row)

        row = 0
        for list in battlefield:
            col = 0
            for item in list:
                item.grid(row=row, column=col, sticky=W)
                col += 1
            row += 1


    def createAIField(self):
        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield_ai']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        battlefield = []
        i = 0
        for r in field:
            row = []
            row.append(Label(self.aifieldboard, text=f"{alphabet[i]}", font=("Arial", 10), height="2",
                             width="5", background=self.bg, foreground=self.fg))

            for char in r:
                if char == '#':
                    row.append(Label(self.aifieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, background=self.sea, foreground=self.bg))
                elif char == 'X':
                    row.append(Label(self.aifieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, background=self.hit, foreground=self.bg))
                else:
                    row.append(Label(self.aifieldboard, font=("Arial", 10), height="2", width="5",
                                     relief=RAISED, foreground=self.bg))

            battlefield.append(row)
            i += 1

        row = []
        row.append(Label(self.aifieldboard, text=f"", font=("Arial", 10), height="2", width="5",
                         background=self.bg, foreground=self.fg))

        for item in range(0,field_size):
            row.append(Label(self.aifieldboard, text=f"{item}", font=("Arial", 10), height="2", width="5",
                             background=self.bg, foreground=self.fg))

        battlefield.append(row)

        row = 0
        for list in battlefield:
            col = 0
            for item in list:
                item.grid(row=row, column=col, sticky=W)
                col += 1
            row += 1


    def update(self):
        self.createField()
        self.fieldboard.after(5000, self.update)