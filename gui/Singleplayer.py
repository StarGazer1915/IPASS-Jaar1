# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# This file displays and runs the window for the Singleplayer mode.
# It also gets the setup information out of the JSON and uses it to
# create a grid and play the game.

# ============ IMPORTS ============ #
from tkinter import *
from gui.Grid import ShowFieldWindow
import random
import json
# ============ GLOBALS ============ #
field_size = 0
amount_of_ships = 0
ships_foundered = 0
ammo = 0

battlefield = [[]]
ship_positions = [[]]

game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ================================= #


class ShowSingleplayer:
    bg = "#0033cc"
    fg = "#ffffff"

    def __init__(self):
        """
        Runs immediately when the class is called.
        Sets global game_over and ships_foundered to false and zero so the game can be replayed
        and the entire program doesn't have to be re-run. Only the setup needs to be re-run
        and the game windows need to be closed. Then it calls the load_json() function to get
        the setup information and then calls the show_singleplayer() function to start the game.

        @return: void
        """
        global game_over
        global ships_foundered

        game_over = False
        ships_foundered = 0

        self.load_json()
        self.show_singleplayer()


    def show_singleplayer(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the Singleplayer window when called.
        It has a button that calls the Grid class and creates a grid and has
        an entry widget for entering a coordinate. It has a button that
        starts the firing sequence with the entered coordinate. Finally it contains
        a text widget that displays information of the game each time the fire
        button is pressed.

        @return: void
        """
        self.SINGLEBOARD = Tk()
        self.SINGLEBOARD.title("Battleship - Singleplayer Board")
        self.SINGLEBOARD.geometry("600x600")
        self.SINGLEBOARD.configure(background=self.bg)
        self.SINGLEBOARD.resizable(0, 0)

        self.SP_LABEL_1 = Label(self.SINGLEBOARD, text="Singleplayer", font=("Arial bold", 40))
        self.SP_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_1.pack()

        self.SP_WHITELINE_1 = Label(self.SINGLEBOARD, font=("Arial bold", 10))
        self.SP_WHITELINE_1.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_1.pack()

        self.SP_BUTTON_1 = Button(self.SINGLEBOARD, text="Show Battlefield", font=("Arial bold", 14))
        self.SP_BUTTON_1.configure(height="2", width="18", command=ShowFieldWindow, highlightbackground=self.bg,foreground=self.bg)
        self.SP_BUTTON_1.pack()

        self.SP_WHITELINE_2 = Label(self.SINGLEBOARD, font=("Arial bold", 10))
        self.SP_WHITELINE_2.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_2.pack()

        self.SP_LABEL_2 = Label(self.SINGLEBOARD, text="Choose a coordinate:", font=("Arial bold", 16))
        self.SP_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_2.pack()

        self.SP_FireEntry = Entry(self.SINGLEBOARD, font=("Arial bold", 16))
        self.SP_FireEntry.configure(highlightbackground=self.bg)
        self.SP_FireEntry.pack()

        self.SP_WHITELINE_3 = Label(self.SINGLEBOARD, font=("Arial bold", 10))
        self.SP_WHITELINE_3.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_3.pack()

        self.SP_FireButton = Button(self.SINGLEBOARD, text="Fire!", font=("Arial bold", 14))
        self.SP_FireButton.configure(height="2", width="8", command=self.fire_shot, highlightbackground=self.bg, foreground=self.bg)
        self.SP_FireButton.pack()

        self.SP_WHITELINE_4 = Label(self.SINGLEBOARD, font=("Arial bold", 10))
        self.SP_WHITELINE_4.configure(background=self.bg, foreground=self.fg)
        self.SP_WHITELINE_4.pack()

        self.SP_LABEL_3 = Label(self.SINGLEBOARD, text="====== Result: ======", font=("Arial bold", 16))
        self.SP_LABEL_3.configure(background=self.bg, foreground=self.fg)
        self.SP_LABEL_3.pack()

        self.SP_TEXTDASH = Text(self.SINGLEBOARD, font=("Arial", 16))
        self.SP_TEXTDASH.config(height="16", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.SP_TEXTDASH.tag_configure("center", justify='center')
        self.SP_TEXTDASH.tag_add("center", 1.0, "end")
        self.SP_TEXTDASH.pack()

        self.create_field()
        self.json_battlefield({'battlefield': battlefield})

        self.SINGLEBOARD.mainloop()


    def create_field(self):
        """
        This function creates a battlefield with the size of field_size.
        It then places ships on the battlefield until it reaches the value of
        amount_of_ships that was extracted from the JSON file. When a ship is
        successfully placed on the battlefield it's coordinates are then added
        to the ship_positions list. It uses the check_place_on_grid() function to
        see if a ship can be placed.

        @return: void
        """
        global battlefield
        global field_size
        global amount_of_ships
        global ship_positions

        rows = field_size
        cols = field_size

        battlefield = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("_")
            battlefield.append(row)

        ships_deployed = 0
        ship_positions = []

        while ships_deployed != amount_of_ships:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(0, cols - 1)
            direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
            ship_size = random.randint(3, 5)
            if self.check_place_on_grid(random_row, random_col, direction, ship_size):
                ships_deployed += 1


    def check_place_on_grid(self, row, col, direction, length):
        """
        This function creates a position for a ship with it's parameters.
        It then uses the check_field_place_ship() function to see if it's
        placement can be done.

        @param row: int
        @param col: int
        @param direction: string
        @param length: int
        @return: boolean
        """
        global field_size

        row_start, row_end, col_start, col_end = row, row+1, col, col+1

        if direction == "LEFT":
            if col - length < 0:
                return False
            col_start = col - length + 1

        elif direction == "RIGHT":
            if col + length >= field_size:
                return False
            col_end = col + length

        elif direction == "UP":
            if row - length < 0:
                return False
            row_start = row - length + 1

        elif direction == "DOWN":
            if row + length >= field_size:
                return False
            row_end = row + length

        return self.check_field_place_ship(row_start, row_end, col_start, col_end)


    def check_field_place_ship(self, row_start, row_end, start_col, end_col):
        """
        This function checks if the given position for a new ship placement
        is allowed/can be done. It looks at the positions and checks if the
        placements do not go outside of the created grid. If the position
        is valid it places the ship on the grid. If the ship has been placed
        correctly it returns True and False if hasn't.

        @param row_start: int
        @param row_end: int
        @param start_col: int
        @param end_col: int
        @return: boolean
        """
        global battlefield
        global ship_positions

        positions_are_valid = True
        for r in range(row_start, row_end):
            for c in range(start_col, end_col):
                if battlefield[r][c] != "_":
                    positions_are_valid = False
                    break

        if positions_are_valid == True:
            ship_positions.append([row_start, row_end, start_col, end_col])
            for r in range(row_start, row_end):
                for c in range(start_col, end_col):
                    battlefield[r][c] = "0"

        return positions_are_valid


    def fire_shot(self):
        """
        This function fires the shot on the battlefield. It gets the coordinate from
        the entry widget and checks if it's not emtpy and the game is not over. If the coordinate
        is not empty it checks if there are no symbols in the coordinate and if the coordinate
        is valid to be used on the battlefield. If it is valid it continues the process in other
        functions and finally checks if the game is over after the shot was fired.

        If the coordinate is not valid it stops the process and gives back a message in the gui's
        text widget. Should the entered coordinate be empty it does this as well. Should the
        variable game_over be True then it stops the game until the user closes all the windows
        except the dashboard.

        NOTE: (I have split up the if statements for readability and priority of conditions)

        @return: void
        """
        global field_size
        global game_over
        global row_letters

        self.SP_TEXTDASH.configure(state=NORMAL)
        self.SP_TEXTDASH.delete('1.0', END)

        shot = self.SP_FireEntry.get().upper()

        if shot != '' and game_over != True:
            letters = re.compile(f'[{row_letters[:field_size]}]')
            symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:-]')

            if symbols.search(shot) != None or letters.search(shot[1:]) != None:
                self.SP_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            elif str(shot[0]) not in row_letters or str(shot[1]) in row_letters:
                self.SP_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            elif len(shot) > 3 or len(shot) <= 1 or int(shot[1:]) >= field_size:
                self.SP_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            else:
                self.fire_sequence(shot)
                self.insert_text()
                self.check_if_game_over()

        elif game_over:
            self.SP_TEXTDASH.insert(END, "The game has ended!\nClose the windows and play again\nfrom the main menu!")
        else:
            self.SP_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")

        self.SP_TEXTDASH.configure(state=DISABLED)


    def fire_sequence(self, shot):
        """
        This function carries out the shooting. It takes the shot and checks
        where the user fired on the battlefield. If the user fires on a position
        where he's/she's already fired before it provides a message and stops.
        This is done to prevent accidentally wasting shots.

        When a shot was hit (or missed) it's symbol on the battlefield will change.
        When a ship was hit it will also check if the ship was foundered with
        the check_ship_foundered() function.

        @param shot: string
        @return: void
        """
        global row_letters
        global battlefield
        global ships_foundered
        global ammo

        self.SP_TEXTDASH.configure(state=NORMAL)
        row, col = row_letters.find(shot[0]), int(shot[1:])

        if battlefield[row][col] == "#" or battlefield[row][col] == "X":
            self.SP_TEXTDASH.insert(END, f"You have already fired a shell here!\n\n")
            self.SP_TEXTDASH.configure(state=DISABLED)
        else:
            if battlefield[row][col] == "_":
                self.SP_TEXTDASH.insert(END, f"You didn't hit anything, try again!\n\n")
                battlefield[row][col] = "#"
            elif battlefield[row][col] == "0":
                self.SP_TEXTDASH.insert(END, f"You hit a ship!\n")
                battlefield[row][col] = "X"
                if self.check_ship_foundered(row, col):
                    self.SP_TEXTDASH.insert(END, f"A ship was foundered!\n\n")
                    ships_foundered += 1

            self.SP_TEXTDASH.configure(state=DISABLED)
            ammo -= 1


    def check_ship_foundered(self, row, col):
        """
        Checks if the ship that was hit has been foundered and returns
        True if it has or False if it hasn't.

        @param row: int
        @param col: int
        @return: boolean
        """
        global ship_positions
        global battlefield

        for position in ship_positions:
            start_row = position[0]
            end_row = position[1]
            start_col = position[2]
            end_col = position[3]
            if start_row <= row <= end_row and start_col <= col <= end_col:
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        if battlefield[r][c] != "X":
                            return False

        return True


    def insert_text(self):
        """
        Handles the extra information that is displayed in the text widget.
        The commented for loop can be uncommented to see the battlefield in real time. (List format)
        After showing the information it runs the json_battlefield() function which updates the
        battlefield in the SingleplayerGame.json file.

        @return: void
        """
        global ammo

        self.SP_TEXTDASH.configure(state=NORMAL)
        self.SP_TEXTDASH.insert(END, f"\nYou've got {ammo} rounds left!\n\n")

        # for i in battlefield:
        #     self.SP_TEXTDASH.insert(END, f"{i}\n")

        self.SP_TEXTDASH.configure(state=DISABLED)
        self.json_battlefield({'battlefield': battlefield})


    def check_if_game_over(self):
        """
        This functions checks various variables to see if the game is over and if
        the player has won. It checks if all ships were foundered or if the ammo has
        been depleted. If so, then the game_over variable will be changed to True and
        the game will end in the fire_shot() function.

        @return: void
        """
        global ships_foundered
        global amount_of_ships
        global ammo
        global game_over

        if amount_of_ships == ships_foundered:
            self.SP_TEXTDASH.configure(state=NORMAL)
            self.SP_TEXTDASH.delete('1.0', END)
            self.SP_TEXTDASH.insert(END, "You won the game!\nCongratulations!")
            self.SP_TEXTDASH.configure(state=DISABLED)
            game_over = True

        elif ammo <= 0:
            self.SP_TEXTDASH.configure(state=NORMAL)
            self.SP_TEXTDASH.delete('1.0', END)
            self.SP_TEXTDASH.insert(END, "You lost!\nYou ran out of bullets!")
            self.SP_TEXTDASH.configure(state=DISABLED)
            game_over = True


    def json_battlefield(self, item):
        """
        Simple function that updates 'item' in the JSON file. An example
        of this is the battlefield that gets updated each time the insert_text()
        function is called.

        @param item: dict
        @return: void
        """
        with open('gui/SingleplayerGame.json', 'r+') as file:
            data = json.load(file)
            data.update(item)
            file.seek(0)
            json.dump(data, file)
            file.close()


    def load_json(self):
        """
        This function reads the SingleplayerGame.json file to extract variables that
        have been set by the user in the setup window. It will then update the global
        variables with these variables to be used in creating the game.

        @return: void
        """
        global field_size
        global amount_of_ships
        global ammo

        with open('gui/SingleplayerGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            amount_of_ships = data['amount_of_ships']
            ammo = data['ammo']
            file.close()