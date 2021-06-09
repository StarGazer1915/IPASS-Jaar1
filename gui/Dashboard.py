from tkinter import *
from gui.Singleplayer import ShowSingleplayer
import json

class ShowBoardGame:
    # ====== Visual Vars ====== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

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
        self.button.configure(height="2", width="28", command=self.showSPSetup, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.button1 = Button(self.dashboard, text="PLAY AGAINST AI", font=("Arial bold", 14))
        self.button1.configure(height="2", width="28", highlightbackground=self.bg, foreground=self.bg)
        self.button1.pack()

        self.dashboard.mainloop()

    def invalidWindow(self):
        self.invalidboard = Tk()
        self.invalidboard.title("Invalid Entry")
        self.invalidboard.geometry("350x200")
        self.invalidboard.configure(background=self.bg)
        self.invalidboard.resizable(0, 0)

        self.label1 = Label(self.invalidboard, text="\nInvalid Entry", font=("Arial 20 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.label1 = Label(self.invalidboard, text="\nThis is not a valid entry!\nTry again.\n", font=("Arial 14 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.button = Button(self.invalidboard, text="Ok", font=("Arial bold", 14))
        self.button.configure(height="2", width="8", command=self.invalidboard.destroy, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.invalidboard.mainloop()

    def showSPSetup(self):
        self.setupboard = Tk()
        self.setupboard.title("Battleship - Singleplayer Setup")
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
        self.button.configure(height="2", width="8", command=self.setupSPCheck, highlightbackground=self.bg, foreground=self.bg)
        self.button.pack()

        self.setupboard.mainloop()


    def setupSPCheck(self):
        size = self.SizeEntry.get()
        ships = self.ShipsEntry.get()
        ammo = self.AmmoEntry.get()
        try:
            if size == '' or ships == '' or ammo == '':
                self.invalidWindow()

            size, ships, ammo = int(size), int(ships), int(ammo)

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
                ShowSingleplayer()

        except TypeError as error:
            print(error)
            self.invalidWindow()
        except ValueError as error:
            pass