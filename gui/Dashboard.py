from tkinter import *

class ShowBoardGame:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ==== Functional Vars ==== #
    #...

    def __init__(self):
        self.showDash()

    def showDash(self):
        self.dashboard = Tk()
        self.dashboard.title("Battleship")
        self.dashboard.geometry("650x400")
        self.dashboard.configure(background=self.bg)
        self.dashboard.resizable(0, 0)

        self.label1 = Label(self.dashboard, text="\nBATTLESHIP", font=("Arial 40 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.label2 = Label(self.dashboard, text="The digital boardgame\n", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.label3 = Label(self.dashboard, text="====== Options: ======\n", font=("Arial 16 bold"))
        self.label3.configure(background=self.bg, foreground=self.fg)
        self.label3.pack()

        self.button = Button(self.dashboard, text="SINGLEPLAYER", font=("Arial bold", 14))
        self.button.configure(height="2", width="28", command=self.showSingleplayer, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.button1 = Button(self.dashboard, text="GAME VS AI", font=("Arial bold", 14))
        self.button1.configure(height="2", width="28", highlightbackground=self.bg, foreground=self.bg)
        self.button1.pack()

        self.dashboard.mainloop()

    def showSingleplayer(self):
        field_size = 10

        self.singleplayer = Tk()
        self.singleplayer.title("Battleship - Singleplayer")
        #self.singleplayer.geometry("650x400")
        self.singleplayer.configure(background=self.bg)

        self.createGrid()

        self.singleplayer.mainloop()

    def createGrid(self):
        field_size = 10
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for r in range(field_size):
            row = []
            row.append(Label(self.singleplayer,
                             text=f"{alphabet[r]}",
                             font=("Arial", 10),
                             height="2",
                             width="5",
                             borderwidth=2,
                             background=self.bg,
                             foreground=self.fg))

            for c in range(field_size):
                row.append(Button(self.singleplayer,
                                  text=f"{alphabet[r]}{c}",
                                  font=("Arial", 10),
                                  height="2",
                                  width="5",
                                  highlightbackground=self.bg,
                                  foreground=self.bg))
                
            for item in range(field_size+1):
                row[item].grid(row=r, column= item, sticky=W)



