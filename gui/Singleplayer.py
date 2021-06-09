from tkinter import *
from gui.Grid import ShowFieldWindow
from gui.Battleship import doBattleshipGame
import random
import json

class ShowSingleplayer:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

    def __init__(self):
        self.showSetup()

    def showSetup(self):
        self.setupboard = Tk()
        self.setupboard.title("Battleship - Singleplayer Board")
        self.setupboard.geometry("350x350")
        self.setupboard.configure(background=self.bg)
        self.setupboard.resizable(0, 0)

        self.label1 = Label(self.setupboard, text="\nINSERT INFORMATION", font=("Arial 20 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.whiteline = Label(self.setupboard, font=("Arial 10 bold"))
        self.whiteline.configure(background=self.bg, foreground=self.fg)
        self.whiteline.pack()

        self.label2 = Label(self.setupboard, text="Battlefield size (10-26):", font=("Arial 14 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()
        self.SizeEntry = Entry(self.setupboard, font=("Arial bold", 16))
        self.SizeEntry.configure(highlightbackground=self.bg)
        self.SizeEntry.pack()

        self.label3 = Label(self.setupboard, text="\nAmount of ships (1-10):", font=("Arial 14 bold"))
        self.label3.configure(background=self.bg, foreground=self.fg)
        self.label3.pack()
        self.ShipsEntry = Entry(self.setupboard, font=("Arial bold", 16))
        self.ShipsEntry.configure(highlightbackground=self.bg)
        self.ShipsEntry.pack()

        self.label3 = Label(self.setupboard, text="\nAmount of shots:", font=("Arial 14 bold"))
        self.label3.configure(background=self.bg, foreground=self.fg)
        self.label3.pack()
        self.AmmoEntry = Entry(self.setupboard, font=("Arial bold", 16))
        self.AmmoEntry.configure(highlightbackground=self.bg)
        self.AmmoEntry.pack()

        self.whiteline3 = Label(self.setupboard, font=("Arial bold", 10))
        self.whiteline3.configure(background=self.bg, foreground=self.fg)
        self.whiteline3.pack()

        self.button = Button(self.setupboard, text="Start", font=("Arial bold", 14))
        self.button.configure(height="2", width="8", command=self.setupCheck, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.setupboard.mainloop()


    def invalidWindow(self):
        self.invalidboard = Tk()
        self.invalidboard.title("Invalid Entry")
        self.invalidboard.geometry("350x200")
        self.invalidboard.configure(background=self.bg)
        self.invalidboard.resizable(0, 0)

        self.label1 = Label(self.invalidboard, text="\nInvalid Entry", font=("Arial 20 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.label1 = Label(self.invalidboard, text="\nThis is not a valid size!\nPick a number between 10 and 26.\n", font=("Arial 14 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.button = Button(self.invalidboard, text="Ok", font=("Arial bold", 14))
        self.button.configure(height="2", width="8", command=self.invalidboard.destroy, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.invalidboard.mainloop()


    def setupCheck(self):
        size = self.SizeEntry.get()
        ships = self.ShipsEntry.get()
        ammo = self.AmmoEntry.get()
        try:
            size = int(size)
            ships = int(ships)
            ammo = int(ammo)
            if size > 26 or size < 10 or ships > 10 or ships <= 0 or ammo <= 0:
                self.invalidWindow()
            else:
                data = {}
                data['field_size'] = size
                data['amount_of_ships'] = ships
                data['ammo'] = ammo
                with open('gui/game.json', 'w') as file:
                    json.dump(data, file)
                    file.close()

                self.setupboard.destroy()
                self.showSingleplayer()
        except TypeError as error:
            print(error)
            self.invalidWindow()


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
        self.textdash.config(height="16", width="80", background=self.bg, foreground="White", highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()
        self.startGame()

        self.singleboard.mainloop()


    def startGame(self):
        self.textdash.configure(state=NORMAL)
        self.textdash.delete('1.0', END)

        print("STARTED GAME")

        pass

    def FireShell(self):
        self.textdash.configure(state=NORMAL)
        self.textdash.delete('1.0', END)

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shot = self.entry.get()

        if shot[0] not in alphabet or shot[1] in alphabet or len(shot) > 2 or len(shot) <= 1:
            self.textdash.insert(END, "That is not a valid coordinate, try again!")
        else:
            self.textdash.insert(END, f"Fired shell at: {shot}\n\n")

        self.textdash.configure(state=DISABLED)
        return
