from tkinter import *
import json

class ShowFieldWindow:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    sea = '#003399'
    hit = '#ff0000'
    # ========================= #

    def __init__(self):
        self.showField()

    def showField(self):
        self.fieldboard = Tk()
        self.fieldboard.title("Battleship - Field")
        self.fieldboard.configure(background=self.bg)
        self.fieldboard.resizable(0,0)

        self.createField()
        self.update()

        self.fieldboard.mainloop()

    def createField(self):
        with open('gui/game.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            field = data['battlefield']
            file.close()

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        battlefield = []
        i = 0
        for r in field:
            row = []
            row.append(Label(self.fieldboard, text=f"{alphabet[i]}", font=("Arial", 10), height="2",
                             width="5", background=self.bg, foreground=self.fg))

            for char in r:
                if char == '#':
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


    def update(self):
        self.createField()
        self.fieldboard.after(5000, self.update)