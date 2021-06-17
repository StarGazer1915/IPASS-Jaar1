# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# This file displays and runs the window for the Player VS AI mode.
# It also gets the setup information out of the JSON and uses it to
# create two grids (player and AI) and play the game.

# ============ IMPORTS ============ #
from tkinter import *
from gui.AI.AIGrid import ShowAIFieldWindows
import random
import json
# ============ GLOBALS ============ #
field_size = 0
amount_of_ships = 0
ships_foundered_pl = 0
ships_foundered_ai = 0
ammo = 0

battlefield_pl = [[]]
battlefield_ai = [[]]
ship_positions_pl = [[]]
ship_positions_ai = [[]]
current_ship = []
ai_shots_missed = []

ai_shell = ''
ai_prev_shell = ['','','']
ai_shot_counter = 0

game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ================================= #


class ShowAIGame:
    bg = "#0033cc"
    fg = "#ffffff"

    def __init__(self):
        """
        Runs immediately when the class is called.
        Sets global variables to false and zero so the game can be replayed and the entire program
        doesn't have to be re-run. Only the setup needs to be re-run and the game windows need to
        be closed. Then it calls the loadJson() function to get the setup information and calls
        the showAIvsPlayer() function to start the game.

        @return: void
        """
        global game_over
        global ships_foundered_pl
        global ships_foundered_ai
        global current_ship
        global ai_shots_missed
        global ai_shot_counter

        game_over = False
        ships_foundered_pl = 0
        ships_foundered_ai = 0
        current_ship = []
        ai_shots_missed = []
        ai_shot_counter = 0

        self.loadJson()
        self.showAIvsPlayer()


    def showAIvsPlayer(self):
        """
        --- TKINTER FUNCTION ---
        This function creates and runs the Player VS AI window when called.
        It has a button that calls the ShowAIFieldWindows class that creates two grids
        and has an entry widget for entering a coordinate. It has a button that
        starts the firing sequence with the entered coordinate, but unlike singleplayer
        it now also starts the turn of the AI simultaneously. Finally it contains
        a text widget that displays information of the game each time the fire
        button is pressed.

        @return: void
        """

        self.AIBOARD = Tk()
        self.AIBOARD.title("Battleship - AI Game Board")
        self.AIBOARD.geometry("550x600")
        self.AIBOARD.configure(background=self.bg)
        self.AIBOARD.resizable(0, 0)

        self.AIG_LABEL_1 = Label(self.AIBOARD, text="Player Versus AI", font=("Arial bold", 40))
        self.AIG_LABEL_1.configure(background=self.bg, foreground=self.fg)
        self.AIG_LABEL_1.pack()

        self.AIG_WHITELINE_1 = Label(self.AIBOARD, font=("Arial bold", 10))
        self.AIG_WHITELINE_1.configure(background=self.bg, foreground=self.fg)
        self.AIG_WHITELINE_1.pack()

        self.AIG_BUTTON_1 = Button(self.AIBOARD, text="Show Battlefield", font=("Arial bold", 14))
        self.AIG_BUTTON_1.configure(height="2", width="18", command=ShowAIFieldWindows, highlightbackground=self.bg,foreground=self.bg)
        self.AIG_BUTTON_1.pack()

        self.AIG_WHITELINE_2 = Label(self.AIBOARD, font=("Arial bold", 10))
        self.AIG_WHITELINE_2.configure(background=self.bg, foreground=self.fg)
        self.AIG_WHITELINE_2.pack()

        self.AIG_LABEL_2 = Label(self.AIBOARD, text="Choose a coordinate:", font=("Arial bold", 16))
        self.AIG_LABEL_2.configure(background=self.bg, foreground=self.fg)
        self.AIG_LABEL_2.pack()

        self.AIG_FireEntry = Entry(self.AIBOARD, font=("Arial bold", 16))
        self.AIG_FireEntry.configure(highlightbackground=self.bg)
        self.AIG_FireEntry.pack()

        self.AIG_WHITELINE_3 = Label(self.AIBOARD, font=("Arial bold", 10))
        self.AIG_WHITELINE_3.configure(background=self.bg, foreground=self.fg)
        self.AIG_WHITELINE_3.pack()

        self.AIG_FireButton = Button(self.AIBOARD, text="Fire!", font=("Arial bold", 14))
        self.AIG_FireButton.configure(height="2", width="8", command=self.firePlayerShot, highlightbackground=self.bg, foreground=self.bg)
        self.AIG_FireButton.pack()

        self.AIG_WHITELINE_4 = Label(self.AIBOARD, font=("Arial bold", 10))
        self.AIG_WHITELINE_4.configure(background=self.bg, foreground=self.fg)
        self.AIG_WHITELINE_4.pack()

        self.AIG_LABEL_3 = Label(self.AIBOARD, text="====== Result: ======", font=("Arial bold", 16))
        self.AIG_LABEL_3.configure(background=self.bg, foreground=self.fg)
        self.AIG_LABEL_3.pack()

        self.AIG_TEXTDASH = Text(self.AIBOARD, font=("Arial", 16))
        self.AIG_TEXTDASH.config(height="16", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.AIG_TEXTDASH.tag_configure("center", justify='center')
        self.AIG_TEXTDASH.tag_add("center", 1.0, "end")
        self.AIG_TEXTDASH.pack()

        self.createFields()
        self.jsonBattlefield({'battlefield_pl': battlefield_pl})
        self.jsonBattlefield({'battlefield_ai': battlefield_ai})

        self.AIBOARD.mainloop()


    def createFields(self):
        """
        This function creates two battlefields with the size of field_size.
        It then places ships on the battlefields until it reaches the value of
        amount_of_ships that was extracted from the JSON file. Unlike the
        singleplayer variant this function has been split into multiple
        functions to accommodate the creation of multiple fields.
        The functions makeField() and makeShipPositions() are
        used to accomplish this.

        @return: void
        """
        global field_size
        global amount_of_ships
        global battlefield_pl
        global battlefield_ai
        global ship_positions_pl
        global ship_positions_ai

        rows, cols = field_size, field_size
        battlefield_pl, battlefield_ai = [], []

        battlefield_pl = self.makeField(battlefield_pl, rows, cols)
        battlefield_ai = self.makeField(battlefield_ai, rows, cols)
        ship_positions_pl = self.makeShipPositions(battlefield_pl, amount_of_ships, rows, cols)
        ship_positions_ai = self.makeShipPositions(battlefield_ai, amount_of_ships, rows, cols)


    def makeField(self, battlefield, rows, cols):
        """
        This function creates the battlefield using the rows and
        columns and returns a two dimensional array.

        @param battlefield: list
        @param rows: int
        @param cols: int
        @return: list
        """
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("_")
            battlefield.append(row)

        return battlefield


    def makeShipPositions(self, battlefield, amount_of_ships, rows, cols):
        """
        This function places ships on the battlefield until it reaches the value of
        amount_of_ships that was extracted from the JSON file. When a ship is
        successfully placed on the battlefield it's coordinates are then added
        to the ship_positions list. It uses the checkPlaceOnGrid() function to
        see if a ship can be placed.

        @param battlefield: list
        @param amount_of_ships: int
        @param rows: int
        @param cols: int
        @return: list
        """
        ships_deployed = 0
        ship_positions = []

        while ships_deployed != amount_of_ships:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(0, cols - 1)
            direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
            ship_size = random.randint(3, 5)
            result = self.checkPlaceOnGrid(battlefield, ship_positions, random_row, random_col, direction, ship_size)
            if not result:
                pass
            elif len(result) > 1:
                if result[0]:
                    ships_deployed += 1

        return ship_positions


    def checkPlaceOnGrid(self, battlefield, ship_positions, row, col, direction, length):
        """
        This function works almost the same as the one used in singleplayer. This function
        has more variables however to support multiple grids. It creates a position for
        a ship with it's parameters. It then uses the checkFieldPlaceShip() function to
        see if it's placement can be done.

        @param battlefield: list
        @param ship_positions: list
        @param row: int
        @param col: int
        @param direction: string
        @param length: int
        @return: list [boolean, list]
        """
        global field_size

        row_start, row_end = row, row+1
        col_start, col_end = col, col+1

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

        result = self.checkFieldPlaceShip(battlefield, ship_positions, row_start, row_end, col_start, col_end)
        return [result[0], result[1]]


    def checkFieldPlaceShip(self, battlefield, ship_positions, row_start, row_end, start_col, end_col):
        """
        This function also works almost identical to the singleplayer variant. It checks
        if the given position for a new ship placement is allowed/can be done. It looks at
        the positions and checks if the placements do not go outside of the created grid.
        If the position is valid it places the ship on the grid. If the ship has been placed
        correctly it returns a list with it's first element being a boolean (True if the ship
        has been placed correctly and False if hasn't) and it's second element being the list
        of ship positions.

        @param battlefield: list
        @param ship_positions: list
        @param row_start: int
        @param row_end: int
        @param start_col: int
        @param end_col: int
        @return: list [boolean, list]
        """
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

        return [positions_are_valid, ship_positions]













    def firePlayerShot(self):
        """
        Works practically the same as the fireShot() function in the singleplayer class.
        This version however calls checkIfGameOver() twice. One after the player has fired
        and one after the fireAIShot() function has been called. (AI has fired)

        *For detailed information see Singleplayer.py docstring of fireShot() function*

        @return: void
        """
        global field_size
        global row_letters
        global game_over
        global battlefield_ai
        global ships_foundered_ai

        self.AIG_TEXTDASH.configure(state=NORMAL)
        self.AIG_TEXTDASH.delete('1.0', END)

        shot = self.AIG_FireEntry.get().upper()

        if shot != '' and game_over != True:

            letters = re.compile(f'[{row_letters[:field_size]}]')
            symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:-]')

            if symbols.search(shot) != None or letters.search(shot[1:]) != None:
                self.AIG_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            elif str(shot[0]) not in row_letters or str(shot[1]) in row_letters:
                self.AIG_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            elif len(shot) > 3 or len(shot) <= 1 or int(shot[1:]) >= field_size:
                self.AIG_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")
            else:
                self.fireSequence(battlefield_ai, ship_positions_ai, ships_foundered_ai, shot)
                self.insertText('battlefield_ai', battlefield_ai)
                self.checkIfGameOver()
                self.fireAIShot()
                self.checkIfGameOver()

        elif game_over:
            self.AIG_TEXTDASH.insert(END, "The game has ended!\nClose the windows and play again\nfrom the main menu!")
        else:
            self.AIG_TEXTDASH.insert(END, "That is not a valid coordinate, try again!")

        self.AIG_TEXTDASH.configure(state=DISABLED)


    def fireSequence(self, battlefield, ship_positions, ships_foundered, shot):
        """
        Works practically the same as the fireSequence() function in the singleplayer class.
        This version however uses parameters instead of globals.

        *For detailed information see Singleplayer.py docstring of fireSequence() function*

        @param battlefield: list
        @param ship_positions: list
        @param ships_foundered: int
        @param shot: string
        @return: void
        """
        global row_letters
        global ammo

        self.AIG_TEXTDASH.configure(state=NORMAL)
        row, col = row_letters.find(shot[0]), int(shot[1:])

        if battlefield[row][col] == "#" or battlefield[row][col] == "X":
            self.AIG_TEXTDASH.insert(END, f"You have already fired a shell here!\n\n")
            self.AIG_TEXTDASH.configure(state=DISABLED)
        else:
            if battlefield[row][col] == "_":
                self.AIG_TEXTDASH.insert(END, f"You didn't hit anything, try again!\n\n")
                battlefield[row][col] = "#"
            elif battlefield[row][col] == "0":
                self.AIG_TEXTDASH.insert(END, f"You hit a ship!\n")
                battlefield[row][col] = "X"
                if self.checkShipFoundered(battlefield, ship_positions, row, col):
                    self.AIG_TEXTDASH.insert(END, f"A ship was foundered!\n\n")
                    ships_foundered += 1

            self.AIG_TEXTDASH.configure(state=DISABLED)
            ammo -= 1


    def checkShipFoundered(self, battlefield, ship_positions, row, col):
        """
        Checks if the ship that was hit has been foundered and returns
        True if it has or False if it hasn't.

        @param battlefield: list
        @param ship_positions: list
        @param row: int
        @param col: int
        @return: boolean
        """
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


    def insertText(self, dataname, battlefield):
        """
        Handles the extra information that is displayed in the text widget.
        The commented for loop can be uncommented to see the battlefield in real time. (List format)
        After showing the information it runs the jsonBattlefield() function which updates the
        battlefield in the AIGame.json file.

        @return: void
        """
        global ammo

        self.AIG_TEXTDASH.configure(state=NORMAL)
        self.AIG_TEXTDASH.insert(END, f"\nYou've got {ammo} rounds left!\n\n")

        for i in battlefield:
            self.AIG_TEXTDASH.insert(END, f"{i}\n")

        self.AIG_TEXTDASH.configure(state=DISABLED)
        self.jsonBattlefield({dataname : battlefield})


    def checkIfGameOver(self):
        """
        This functions checks various variables to see if the game is over and if
        the player or AI has won. It checks if all ships of either party were foundered
        or if the ammo has been depleted. If so, then the game_over variable will be
        changed to True and the game will end in the firePlayerShot() function.

        @return: void
        """
        global ships_foundered_ai
        global ships_foundered_pl
        global amount_of_ships
        global ammo
        global game_over

        if amount_of_ships == ships_foundered_ai:
            self.AIG_TEXTDASH.configure(state=NORMAL)
            self.AIG_TEXTDASH.delete('1.0', END)
            self.AIG_TEXTDASH.insert(END, "You won the game!\nYou foundered all enemy ships!")
            self.AIG_TEXTDASH.configure(state=DISABLED)
            game_over = True
        elif amount_of_ships == ships_foundered_pl:
            self.AIG_TEXTDASH.configure(state=NORMAL)
            self.AIG_TEXTDASH.delete('1.0', END)
            self.AIG_TEXTDASH.insert(END, "You lost the game!\nThe AI has sunk all your ships!")
            self.AIG_TEXTDASH.configure(state=DISABLED)
            game_over = True
        elif ammo <= 0:
            self.AIG_TEXTDASH.configure(state=NORMAL)
            self.AIG_TEXTDASH.delete('1.0', END)
            self.AIG_TEXTDASH.insert(END, "You lost!\nYou ran out of bullets!")
            self.AIG_TEXTDASH.configure(state=DISABLED)
            game_over = True


    def fireAIShot(self):
        """
        This is the AI equivalent of the firePlayerShot() function. However, this function
        is significantly smaller because we don't need to check if the AI gives a valid
        coordinate.

        @return: void
        """
        global battlefield_pl
        global ship_positions_pl

        if not game_over:
            self.AI(battlefield_pl, ship_positions_pl)
            self.jsonBattlefield({'battlefield_pl' : battlefield_pl})
            self.checkIfGameOver()


    def AI(self, battlefield_pl, ship_positions_pl):
        """
        This is the AI function of the game. It follows the algorithm of the
        shape S ⊂ Z^2 shape from the 'University Clermont Auvergne' in France.

        Source: https://pageperso.lis-lab.fr/guilherme.fonseca/battleship_conf.pdf
        (Page 5 is the algorithm that I implemented)

        --- HOW IT WORKS: ---
        The AI shoots randomly like a human player possibly would until it hits a ship.
        This first hit will be seen as the first position. The AI will then start firing
        more accurately around that location.

        When it hits a ship it will follow a pattern that shoots in several directions
        in a specific order: Left, Right, Up, Down. It does this until it hits the sea and
        then resets it's targeting to the original hit. Ships in this Battleship game are
        only ever placed in vertical or horizontal directions. This means that we only need
        to shoot in four directions until we reach the sea (Sea = Miss) and if the
        ship is still not foundered (Sunk) after one direction then reset and try another.

        --- MORE INFO: ---
        In this function I have a counter counting the amount of shots in a specific direction.
        When the shot misses it will increase the counter so it starts shooting in another
        direction. Should the shots hit then it will keep shooting up to 4 times in that
        direction until it misses. When a ship is foundered it resets the counter and returns
        to firing randomly. It adds misses and hits to a list that will act as its memory, it
        checks if it already fired at a specific location and if so, it chooses another coordinate
        before launching it's attack.

        This function uses the fireAISequence() function to fire it's shots.

        @param battlefield_pl: list
        @param ship_positions_pl: list
        @return: void
        """
        global ai_shell
        global ai_prev_shell
        global current_ship
        global ai_shots_missed
        global ai_shot_counter
        global row_letters
        global field_size

        used_letters = row_letters[:field_size]

        if current_ship == []:
            while True:
                ai_shell = random.choice(used_letters) + str(random.randint(0, field_size-1))
                if ai_shell not in ai_shots_missed:
                    break

            ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, ai_shell)
            if ai_prev_shell[0] == 'hit':
                current_ship.append(ai_prev_shell[1])
                ai_shots_missed.append(ai_prev_shell[1])
            else:
                ai_shots_missed.append(ai_prev_shell[1])

        # ==== FIRST POSITION FOUND, START FOCUS FIRING ==== #
        elif len(current_ship) >= 1:

            # Fire left until a shot misses, should it exit the grid it will return to it's first hit. #
            if ai_shot_counter <= 4:
                try:
                    newshot = ai_prev_shell[1][0] + str(int(ai_prev_shell[1][1]) - 1)
                    ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)

                    if ai_prev_shell[0] in ['hit','already_hit']:
                        ai_shots_missed.append(ai_prev_shell[1])
                    elif ai_prev_shell[0] in ['miss','already_miss','']:
                        ai_shots_missed.append(ai_prev_shell[1])
                        ai_shot_counter = 4

                    if ai_prev_shell[2] == 'foundered':
                        current_ship = []
                        ai_shot_counter = 0

                    ai_shot_counter += 1
                    if ai_shot_counter == 5:
                        ai_prev_shell[1] = current_ship[0]
                        return

                except (IndexError, ValueError):
                    print(f"Algorithm went out of grid. Resetting...")
                    ai_shot_counter = 5
                    ai_prev_shell[1] = current_ship[0]

            else:
                # Fire right until a shot misses, should it exit the grid it will return to it's first hit. #
                if ai_shot_counter <= 8:
                    try:
                        newshot = ai_prev_shell[1][0] + str(int(ai_prev_shell[1][1]) + 1)
                        ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)

                        if ai_prev_shell[0] in ['hit', 'already_hit']:
                            ai_shots_missed.append(ai_prev_shell[1])
                        elif ai_prev_shell[0] in ['miss', 'already_miss', '']:
                            ai_shots_missed.append(ai_prev_shell[1])
                            ai_shot_counter = 8

                        if ai_prev_shell[2] == 'foundered':
                            current_ship = []
                            ai_shot_counter = 0

                        ai_shot_counter += 1
                        if ai_shot_counter == 9:
                            ai_prev_shell[1] = current_ship[0]
                            return

                    except (IndexError, ValueError):
                        print("Algorithm went out of grid, Resetting...")
                        ai_shot_counter = 9
                        ai_prev_shell[1] = current_ship[0]

                else:
                    # Fire upwards until a shot misses, should it exit the grid it will return to it's first hit. #
                    if ai_shot_counter <= 12:
                        try:
                            top = used_letters[used_letters.index(ai_prev_shell[1][0]) - 1]
                            newshot = top + ai_prev_shell[1][1]
                            ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)

                            if ai_prev_shell[0] in ['hit', 'already_hit']:
                                ai_shots_missed.append(ai_prev_shell[1])
                            elif ai_prev_shell[0] in ['miss', 'already_miss', '']:
                                ai_shots_missed.append(ai_prev_shell[1])
                                ai_shot_counter = 12

                            if ai_prev_shell[2] == 'foundered':
                                current_ship = []
                                ai_shot_counter = 0

                            ai_shot_counter += 1
                            if ai_shot_counter == 13:
                                ai_prev_shell[1] = current_ship[0]
                                return

                        except (IndexError, ValueError):
                            print("Algorithm went out of grid, Resetting...")
                            ai_shot_counter = 13
                            ai_prev_shell[1] = current_ship[0]

                    else:
                        # Fire downwards until a shot misses, should it exit the grid it will return to it's originial hit. #
                        if ai_shot_counter <= 16:
                            try:
                                bottom = used_letters[used_letters.index(ai_prev_shell[1][0]) + 1]
                                newshot = bottom + ai_prev_shell[1][1]
                                ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)

                                if ai_prev_shell[0] in ['hit', 'already_hit']:
                                    ai_shots_missed.append(ai_prev_shell[1])
                                elif ai_prev_shell[0] in ['miss', 'already_miss', '']:
                                    ai_shots_missed.append(ai_prev_shell[1])
                                    ai_shot_counter = 16

                                if ai_prev_shell[2] == 'foundered':
                                    current_ship = []
                                    ai_shot_counter = 0

                                ai_shot_counter += 1
                                if ai_shot_counter == 17:
                                    ai_prev_shell[1] = current_ship[0]
                                    return

                            except (IndexError, ValueError):
                                print("Algorithm went out of grid, Resetting...")
                                ai_shot_counter = 17
                                ai_prev_shell[1] = current_ship[0]

                        else:
                            current_ship = []
                            ai_shot_counter = 0


    def fireAISequence(self, battlefield_pl, ship_positions_pl, shot):
        """
        This function works practically the same as the fireSequence() function
        for the player. This function however determines if the AI has already
        fired on a coordinate in a different way. It stores information in a
        list (result) that it then gives back to the AI in a way the game would
        to a human player. (It was a hit, a ship was foundered, etc.)

        @param battlefield_pl: list
        @param ship_positions_pl: list
        @param shot: string
        @return: list
        """
        global row_letters
        global ammo
        global ships_foundered_pl

        result = ['','','']
        result[1] = shot

        row, col = row_letters.find(shot[0]), int(shot[1:])

        if battlefield_pl[row][col] == "_":
            result[0] = 'miss'
            battlefield_pl[row][col] = "#"
        elif battlefield_pl[row][col] == "#":
            result[0] = 'already_missed'
            battlefield_pl[row][col] = "#"
        elif battlefield_pl[row][col] == "X":
            result[0] = 'already_hit'
            battlefield_pl[row][col] = "X"
        elif battlefield_pl[row][col] == "0":
            result[0] = 'hit'
            battlefield_pl[row][col] = "X"
            if self.checkShipFoundered(battlefield_pl, ship_positions_pl, row, col):
                result[2] = 'foundered'
                ships_foundered_pl += 1

        return result


    def jsonBattlefield(self, item):
        """
        Simple function that updates 'item' in the JSON file. An example
        of this is the battlefield that gets updated each time the insertText()
        function is called.

        @param item: dict
        @return: void
        """
        with open('gui/AI/AIGame.json', 'r+') as file:
            data = json.load(file)
            data.update(item)
            file.seek(0)
            json.dump(data, file)
            file.close()


    def loadJson(self):
        """
        This function reads the AIGame.json file to extract variables that
        have been set by the user in the setup window. It will then update the global
        variables with these variables to be used in creating the game.

        @return: void
        """
        global field_size
        global amount_of_ships
        global ammo

        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            amount_of_ships = data['amount_of_ships']
            ammo = data['ammo']
            file.close()