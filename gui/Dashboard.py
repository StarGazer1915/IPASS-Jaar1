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
        self.button.configure(height="2", width="28", highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.button1 = Button(self.dashboard, text="GAME VS AI", font=("Arial bold", 14))
        self.button1.configure(height="2", width="28", highlightbackground=self.bg, foreground=self.bg)
        self.button1.pack()

        self.dashboard.mainloop()