# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# This file displays the initial window and setup windows.
# It also handles the setup information and writes it to the JSON files.

# ============ IMPORTS ============ #
from tkinter import *
from gui.Singleplayer import ShowSingleplayer
from gui.AI.AI import ShowAIGame
import json
# ================================= #


class ShowBoardGame:
    bg = "#0033cc"
    fg = "#ffffff"

    def __init__(self):
        """
        Runs the self.showDash() function when the class is called.
        @return: void
        """
        self.showDash()

    def showDash(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the Dashboard window when called.
        @return: void
        """
        self.DASHBOARD = Tk()
        self.DASHBOARD.title("Battleship - Dashboard")
        self.DASHBOARD.geometry("650x400")
        self.DASHBOARD.configure(background=self.bg)
        self.DASHBOARD.resizable(0, 0)

        self.DB_LABEL_1 = Label(self.DASHBOARD, text="\nBATTLESHIP", font=("Arial bold", 40))
        self.DB_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.DB_LABEL_1.pack()

        self.DB_LABEL_2 = Label(self.DASHBOARD, text="The digital boardgame!\n", font=("Arial bold", 16))
        self.DB_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.DB_LABEL_2.pack()

        self.DB_LABEL_3 = Label(self.DASHBOARD, text="====== Options: ======\n", font=("Arial bold", 16))
        self.DB_LABEL_3.configure(background=self.bg, foreground=self.fg)
        self.DB_LABEL_3.pack()

        self.DB_BUTTON_1 = Button(self.DASHBOARD, text="SINGLEPLAYER", font=("Arial bold", 14))
        self.DB_BUTTON_1.configure(height="2", width="28", command=self.showSPSetup, highlightbackground=self.bg, foreground=self.bg)
        self.DB_BUTTON_1.pack()

        self.DB_BUTTON_2 = Button(self.DASHBOARD, text="PLAY AGAINST AI", font=("Arial bold", 14))
        self.DB_BUTTON_2.configure(height="2", width="28", command=self.showAISetup, highlightbackground=self.bg, foreground=self.bg)
        self.DB_BUTTON_2.pack()

        self.DASHBOARD.mainloop()


    def invalidWindow(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the 'invalid window' when called.
        This window is usually used when an entry is invalid. It automatically
        closes itself when the button is pressed.

        @return: void
        """
        self.INVALIDBOARD = Tk()
        self.INVALIDBOARD.title("Invalid Entry")
        self.INVALIDBOARD.geometry("350x200")
        self.INVALIDBOARD.configure(background=self.bg)
        self.INVALIDBOARD.resizable(0, 0)

        self.INV_LABEL_1 = Label(self.INVALIDBOARD, text="\nInvalid Entry", font=("Arial bold", 20))
        self.INV_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.INV_LABEL_1.pack()

        self.INV_LABEL_2 = Label(self.INVALIDBOARD, text="\nThis is not a valid entry!\n", font=("Arial bold", 14))
        self.INV_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.INV_LABEL_2.pack()

        self.INV_BUTTON_1 = Button(self.INVALIDBOARD, text="Ok", font=("Arial bold", 14))
        self.INV_BUTTON_1.configure(height="2", width="8", command=self.INVALIDBOARD.destroy, highlightbackground=self.bg, foreground=self.bg)
        self.INV_BUTTON_1.pack()

        self.INVALIDBOARD.mainloop()


    def showSPSetup(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the setup window for the Singleplayer mode.
        Information can be entered here that will be stored into a JSON file
        using the setupSPCheck() function.

        @return: void
        """
        self.SETUPBOARD_SP = Tk()
        self.SETUPBOARD_SP.title("Battleship - Singleplayer Setup")
        self.SETUPBOARD_SP.geometry("350x350")
        self.SETUPBOARD_SP.configure(background=self.bg)
        self.SETUPBOARD_SP.resizable(0, 0)

        self.SP_LABEL_1 = Label(self.SETUPBOARD_SP, text="\nINSERT INFORMATION", font=("Arial bold", 20))
        self.SP_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_1.pack()

        self.SP_WHITELINE_1 = Label(self.SETUPBOARD_SP, font=("Arial bold", 10))
        self.SP_WHITELINE_1.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_1.pack()

        self.SP_LABEL_2 = Label(self.SETUPBOARD_SP, text="Battlefield size (10-26):", font=("Arial bold", 14))
        self.SP_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_2.pack()

        self.SP_SizeEntry = Entry(self.SETUPBOARD_SP, font=("Arial bold", 16))
        self.SP_SizeEntry.configure(highlightbackground=self.bg)
        self.SP_SizeEntry.pack()

        self.SP_LABEL_3 = Label(self.SETUPBOARD_SP, text="\nAmount of ships (1-10):", font=("Arial bold", 14))
        self.SP_LABEL_3.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_3.pack()

        self.SP_ShipsEntry = Entry(self.SETUPBOARD_SP, font=("Arial bold", 16))
        self.SP_ShipsEntry.configure(highlightbackground=self.bg)
        self.SP_ShipsEntry.pack()

        self.SP_LABEL_4 = Label(self.SETUPBOARD_SP, text="\nAmount of shots:", font=("Arial bold", 14))
        self.SP_LABEL_4.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_4.pack()

        self.SP_AmmoEntry = Entry(self.SETUPBOARD_SP, font=("Arial bold", 16))
        self.SP_AmmoEntry.configure(highlightbackground=self.bg)
        self.SP_AmmoEntry.pack()

        self.SP_WHITELINE_2 = Label(self.SETUPBOARD_SP, font=("Arial bold", 10))
        self.SP_WHITELINE_2.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_2.pack()

        self.SP_BUTTON_1 = Button(self.SETUPBOARD_SP, text="Start", font=("Arial bold", 14))
        self.SP_BUTTON_1.configure(height="2", width="8", command=self.setupSPCheck, highlightbackground=self.bg, foreground=self.bg)
        self.SP_BUTTON_1.pack()

        self.SETUPBOARD_SP.mainloop()


    def setupSPCheck(self):
        """
        Gets setupinformation from the Singleplayer setup window.
        Checks if these values are not '' and if they are all integers. If not then
        the invalid window is called and the user is asked to enter the information again.
        If the entered info is acceptable it writes it to gui/SingleplayerGame.json (deleting
        any previously stored data for re-playability) and starts the Singleplayer mode while
        closing the setup window.

        @return: void
        """
        size = self.SP_SizeEntry.get()
        ships = self.SP_ShipsEntry.get()
        ammo = self.SP_AmmoEntry.get()
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
                with open('gui/SingleplayerGame.json', 'w') as file:
                    json.dump(data, file)
                    file.close()

                self.SETUPBOARD_SP.destroy()
                ShowSingleplayer()

        except TypeError:
            self.invalidWindow()
        except ValueError:
            pass


    def showAISetup(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the setup window for the Player VS AI mode.
        Information can be entered here that will be stored into a JSON file
        using the setupAICheck() function.

        @return: void
        """
        self.SETUPBOARD_AI = Tk()
        self.SETUPBOARD_AI.title("Battleship - AI Setup")
        self.SETUPBOARD_AI.geometry("350x350")
        self.SETUPBOARD_AI.configure(background=self.bg)
        self.SETUPBOARD_AI.resizable(0, 0)

        self.AI_LABEL_1 = Label(self.SETUPBOARD_AI, text="\nINSERT INFORMATION", font=("Arial bold", 20))
        self.AI_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.AI_LABEL_1.pack()

        self.AI_WHITELINE_1 = Label(self.SETUPBOARD_AI, font=("Arial bold", 10))
        self.AI_WHITELINE_1.configure(background=self.bg, foreground=self.fg)
        self.AI_WHITELINE_1.pack()

        self.AI_LABEL_2 = Label(self.SETUPBOARD_AI, text="Battlefield size (10-26):", font=("Arial bold", 14))
        self.AI_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.AI_LABEL_2.pack()

        self.AI_SizeEntry = Entry(self.SETUPBOARD_AI, font=("Arial bold", 16))
        self.AI_SizeEntry.configure(highlightbackground=self.bg)
        self.AI_SizeEntry.pack()

        self.AI_LABEL_3 = Label(self.SETUPBOARD_AI, text="\nAmount of ships (1-10):", font=("Arial bold", 14))
        self.AI_LABEL_3.configure(background=self.bg, foreground=self.fg)
        self.AI_LABEL_3.pack()

        self.AI_ShipsEntry = Entry(self.SETUPBOARD_AI, font=("Arial bold", 16))
        self.AI_ShipsEntry.configure(highlightbackground=self.bg)
        self.AI_ShipsEntry.pack()

        self.AI_LABEL_4 = Label(self.SETUPBOARD_AI, text="\nAmount of shots:", font=("Arial bold", 14))
        self.AI_LABEL_4.configure(background=self.bg, foreground=self.fg)
        self.AI_LABEL_4.pack()

        self.AI_AmmoEntry = Entry(self.SETUPBOARD_AI, font=("Arial bold", 16))
        self.AI_AmmoEntry.configure(highlightbackground=self.bg)
        self.AI_AmmoEntry.pack()

        self.AI_WHITELINE_2 = Label(self.SETUPBOARD_AI, font=("Arial bold", 10))
        self.AI_WHITELINE_2.configure(background=self.bg, foreground=self.fg)
        self.AI_WHITELINE_2.pack()

        self.AI_BUTTON_1 = Button(self.SETUPBOARD_AI, text="Start", font=("Arial bold", 14))
        self.AI_BUTTON_1.configure(height="2", width="8", command=self.setupAICheck, highlightbackground=self.bg, foreground=self.bg)
        self.AI_BUTTON_1.pack()

        self.SETUPBOARD_AI.mainloop()


    def setupAICheck(self):
        """
        Gets setupinformation from the Player VS AI setup window.
        Works exactly the same as the setupSPCheck() function. However, this
        function starts the Player VS AI mode mode instead of the Singleplayer mode.

        @return: void
        """
        size = self.AI_SizeEntry.get()
        ships = self.AI_ShipsEntry.get()
        ammo = self.AI_AmmoEntry.get()
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
                with open('gui/AI/AIGame.json', 'w') as file:
                    json.dump(data, file)
                    file.close()

                self.SETUPBOARD_AI.destroy()
                ShowAIGame()

        except TypeError:
            self.invalidWindow()
        except ValueError:
            pass
