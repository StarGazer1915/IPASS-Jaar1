from tkinter import *

class ShowBoardGame:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ==== Functional Vars ==== #
    #...

    def __init__(self):
        self.showGame()

    def showGame(self):
        self.dashboard = Tk()
        self.dashboard.title("Battleship")
        self.dashboard.geometry("1200x600")
        self.dashboard.configure(background=self.bg)
        self.dashboard.resizable(0, 0)

        self.label1 = Label(self.dashboard, text="\nBATTLESHIP", font=("Arial 40 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.label2 = Label(self.dashboard, text="The digital boardgame\n", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.textdash = Text(self.dashboard, font=("Arial", 16))
        self.textdash.config(height="22", width="80", background=self.bg, foreground="White",highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()
        self.displayField()

        self.dashboard.mainloop()

    def displayField(self):
        field_size = 10

        field = []
        for row in range(field_size):
            newrow = []
            for col in range(field_size):
                newrow.append(" O ")
            field.append(newrow)

        for i in field:
            self.textdash.insert(END, f'{i}\n')

        return