from tkinter import *
from gui.Grid import ShowFieldWindow

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
        self.singleboard.geometry("650x500")
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

        self.entry = Entry(self.singleboard, font=("Arial bold", 16))
        self.entry.configure(highlightbackground=self.bg)
        self.entry.pack()

        self.whiteline3 = Label(self.singleboard, font=("Arial bold", 10))
        self.whiteline3.configure(background=self.bg, foreground=self.fg)
        self.whiteline3.pack()

        self.button = Button(self.singleboard, text="Fire!", font=("Arial bold", 14))
        self.button.configure(height="2", width="8", command="", highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.whiteline4 = Label(self.singleboard, font=("Arial 10 bold"))
        self.whiteline4.configure(background=self.bg, foreground=self.fg)
        self.whiteline4.pack()

        self.label2 = Label(self.singleboard, text="====== Result: ======", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.textdash = Text(self.singleboard, font=("Arial bold", 16))
        self.textdash.config(height="11", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()

        self.singleboard.mainloop()
