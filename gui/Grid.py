from tkinter import *

class ShowFieldWindow:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

    def __init__(self):
        self.showField()

    def showField(self):
        self.fieldboard = Tk()
        self.fieldboard.title("Battleship - Field")
        self.fieldboard.configure(background=self.bg)
        self.fieldboard.resizable(0,0)
        self.createField()

        self.fieldboard.mainloop()

    def createField(self):
        field_size = 10 # Cannot be more than alphabet length (26) !!!
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        battlefield = []
        for r in range(field_size):
            row = []
            row.append(Label(self.fieldboard,
                             text=f"{alphabet[r]}",
                             font=("Arial", 10),
                             height="2",
                             width="5",
                             borderwidth=2,
                             background=self.bg,
                             foreground=self.fg))

            for c in range(1,field_size):
                row.append(Label(self.fieldboard,
                                  font=("Arial", 10),
                                  height="2",
                                  width="5",
                                  relief=RAISED,
                                  foreground=self.bg))

            battlefield.append(row)

        row = []
        for item in range(0,field_size):
            row.append(Label(self.fieldboard,
                             text=f"{item}",
                             font=("Arial", 10),
                             height="2",
                             width="5",
                             borderwidth=2,
                             background=self.bg,
                             foreground=self.fg))

        battlefield.append(row)

        row = 0
        for list in battlefield:
            col = 0
            for item in list:
                item.grid(row=row, column=col, sticky=W)
                col += 1
            row += 1
