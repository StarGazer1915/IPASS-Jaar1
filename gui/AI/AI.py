# ============ STUDENT ============ #
#   Naam:       Justin Klein
#   Klas:       V1B
#   Nummer:     1707815
#   Project:    IPASS
# ================================= #

# ============ IMPORTS ============ #
from tkinter import *
from gui.AI.AIGrid import ShowAIFieldWindows
import random
import json

# ============ GLOBALS ============ #
field_size = 0
amount_of_ships = 0
ammo = 0

ship_min_size = 3
ship_max_size = 5

ships_foundered_pl = 0
ships_foundered_ai = 0
battlefield_pl = [[]]
battlefield_ai = [[]]
ship_positions_pl = [[]]
ship_positions_ai = [[]]
current_ship = []
ai_shots_missed = []
ai_shell = ''
ai_prev_shell = ['','']
ai_shot_counter = 0

game_over = False
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ================================= #


class ShowAIGame:
    # ======== Visuals ======== #
    bg = "#0033cc"
    fg = "#ffffff"
    # ========================= #

    def __init__(self):
        global game_over
        game_over = False

        global ships_foundered_pl
        global ships_foundered_ai
        global current_ship
        global ai_shots_missed
        global ai_shot_counter
        ships_foundered_pl = 0
        ships_foundered_ai = 0
        current_ship = []
        ai_shots_missed = []
        ai_shot_counter = 0

        self.loadJson()
        self.showAIvsPlayer()


    def showAIvsPlayer(self):
        self.aiboard = Tk()
        self.aiboard.title("Battleship - AI Game Board")
        self.aiboard.geometry("550x600")
        self.aiboard.configure(background=self.bg)
        self.aiboard.resizable(0, 0)

        self.label1 = Label(self.aiboard, text="Player Versus AI", font=("Arial 40 bold"))
        self.label1.configure(background=self.bg, foreground=self.fg)
        self.label1.pack()

        self.whiteline = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline.configure(background=self.bg, foreground=self.fg)
        self.whiteline.pack()

        self.button = Button(self.aiboard, text="Show Battlefield", font=("Arial bold", 14))
        self.button.configure(height="2", width="18", command=ShowAIFieldWindows, highlightbackground=self.bg,foreground=self.bg)
        self.button.pack()

        self.whiteline2 = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline2.configure(background=self.bg, foreground=self.fg)
        self.whiteline2.pack()

        self.label2 = Label(self.aiboard, text="Choose a coordinate:", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.FireEntry = Entry(self.aiboard, font=("Arial bold", 16))
        self.FireEntry.configure(highlightbackground=self.bg)
        self.FireEntry.pack()

        self.whiteline3 = Label(self.aiboard, font=("Arial bold", 10))
        self.whiteline3.configure(background=self.bg, foreground=self.fg)
        self.whiteline3.pack()

        self.FireButton = Button(self.aiboard, text="Fire!", font=("Arial bold", 14))
        self.FireButton.configure(height="2", width="8", command=self.firePlayerShot, highlightbackground=self.bg, foreground=self.bg)
        self.FireButton.pack()

        self.whiteline4 = Label(self.aiboard, font=("Arial 10 bold"))
        self.whiteline4.configure(background=self.bg, foreground=self.fg)
        self.whiteline4.pack()

        self.label2 = Label(self.aiboard, text="====== Result: ======", font=("Arial 16 bold"))
        self.label2.configure(background=self.bg, foreground=self.fg)
        self.label2.pack()

        self.textdash = Text(self.aiboard, font=("Arial", 16))
        self.textdash.config(height="16", width="40", background=self.bg, foreground="White", highlightbackground="grey")
        self.textdash.tag_configure("center", justify='center')
        self.textdash.tag_add("center", 1.0, "end")
        self.textdash.pack()

        self.createFields()
        self.jsonBattlefield({'battlefield_pl': battlefield_pl})
        self.jsonBattlefield({'battlefield_ai': battlefield_ai})

        self.aiboard.mainloop()


    def makeField(self, battlefield, rows, cols):
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("_")
            battlefield.append(row)

        return battlefield


    def makeShipPositions(self, battlefield, ship_positions, amount_of_ships, rows, cols):
        ships_deployed, ship_positions = 0, []

        while ships_deployed != amount_of_ships:
            random_row = random.randint(0, rows - 1)
            random_col = random.randint(0, cols - 1)
            direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
            ship_size = random.randint(ship_min_size, ship_max_size)
            result = self.checkPlaceOnGrid(battlefield, ship_positions, random_row, random_col, direction, ship_size)
            if not result:
                pass
            elif len(result) > 1:
                if result[0]:
                    ships_deployed += 1

        return ship_positions


    def checkPlaceOnGrid(self, battlefield, ship_positions, row, col, direction, length):
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

        result = self.checkFieldPlaceShip(battlefield, ship_positions, row_start, row_end, col_start, col_end)
        return [result[0], result[1]]


    def checkFieldPlaceShip(self, battlefield, ship_positions, row_start, row_end, start_col, end_col):
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


    def createFields(self):
        global field_size
        global amount_of_ships
        global ship_min_size
        global ship_max_size
        global battlefield_pl
        global battlefield_ai
        global ship_positions_pl
        global ship_positions_ai

        rows, cols = field_size, field_size
        battlefield_pl, battlefield_ai = [], []

        battlefield_pl = self.makeField(battlefield_pl, rows, cols)
        battlefield_ai = self.makeField(battlefield_ai, rows, cols)
        ship_positions_pl = self.makeShipPositions(battlefield_pl, ship_positions_pl, amount_of_ships, rows, cols)
        ship_positions_ai = self.makeShipPositions(battlefield_ai, ship_positions_ai, amount_of_ships, rows, cols)


    def checkShellShot(self, battlefield, shot):
        global row_letters

        row, col = shot[0], shot[1:]
        row, col = row_letters.find(row), int(col)

        if battlefield[row][col] == "#" or battlefield[row][col] == "X":
            self.textdash.configure(state=NORMAL)
            self.textdash.insert(END, f"You have already fired a shell here!\n\n")
            self.textdash.configure(state=DISABLED)

        return row, col


    def fireSequence(self, battlefield, ship_positions, ships_foundered, shot):
        global ammo

        self.textdash.configure(state=NORMAL)
        row, col = self.checkShellShot(battlefield, shot)

        if battlefield[row][col] == "_":
            self.textdash.insert(END, f"You didn't hit anything, try again!\n\n")
            battlefield[row][col] = "#"
        elif battlefield[row][col] == "0":
            self.textdash.insert(END, f"You hit a ship!\n")
            battlefield[row][col] = "X"
            if self.checkShipFoundered(battlefield, ship_positions, row, col):
                self.textdash.insert(END, f"A ship was foundered!\n\n")
                ships_foundered += 1

        self.textdash.configure(state=DISABLED)
        ammo -= 1


    def checkShipFoundered(self, battlefield, ship_positions, row, col):
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


    def checkIfGameOver(self):
        global ships_foundered_ai
        global ships_foundered_pl
        global amount_of_ships
        global ammo
        global game_over

        if amount_of_ships == ships_foundered_ai:
            self.textdash.configure(state=NORMAL)
            self.textdash.delete('1.0', END)
            self.textdash.insert(END, "You won the game!\nYou foundered all enemy ships!")
            self.textdash.configure(state=DISABLED)
            game_over = True
        elif amount_of_ships == ships_foundered_pl:
            self.textdash.configure(state=NORMAL)
            self.textdash.delete('1.0', END)
            self.textdash.insert(END, "You lost the game!\nThe AI has sunk all your ships!")
            self.textdash.configure(state=DISABLED)
            game_over = True
        elif ammo <= 0:
            self.textdash.configure(state=NORMAL)
            self.textdash.delete('1.0', END)
            self.textdash.insert(END, "You lost!\nYou ran out of bullets!")
            self.textdash.configure(state=DISABLED)
            game_over = True


    def firePlayerShot(self):
        global field_size
        global row_letters
        global battlefield_ai
        global ships_positions_ai
        global ships_foundered_ai

        self.textdash.configure(state=NORMAL)
        self.textdash.delete('1.0', END)

        shot = self.FireEntry.get().upper()

        if shot != '' and game_over != True:

            letters = re.compile(f'[{row_letters[:field_size]}]')
            symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:-]')

            if symbols.search(shot) != None or letters.search(shot[1:]) != None:
                self.textdash.insert(END, "That is not a valid coordinate, try again!")
            elif str(shot[0]) not in row_letters or str(shot[1]) in row_letters:
                self.textdash.insert(END, "That is not a valid coordinate, try again!")
            elif len(shot) > 3 or len(shot) <= 1 or int(shot[1:]) >= field_size:
                self.textdash.insert(END, "That is not a valid coordinate, try again!")
            else:
                self.fireSequence(battlefield_ai, ship_positions_ai, ships_foundered_ai, shot)
                self.insertText('battlefield_ai', battlefield_ai)
                self.checkIfGameOver()
                self.fireAIShot()
                self.checkIfGameOver()

        elif game_over:
            self.textdash.insert(END, "The game has ended!\nClose the windows and play again\nfrom the main menu!")
        else:
            self.textdash.insert(END, "That is not a valid coordinate, try again!")

        self.textdash.configure(state=DISABLED)


    def fireAIShot(self):
        global battlefield_pl
        global ships_positions_pl
        global ships_foundered_pl

        if not game_over:
            self.AI(battlefield_pl, ship_positions_pl, ships_foundered_pl)
            self.jsonBattlefield({'battlefield_pl' : battlefield_pl})
            self.checkIfGameOver()


    def AI(self, battlefield_pl, ship_positions_pl, ships_foundered_pl):
        global ai_shell
        global ai_prev_shell
        global current_ship
        global ai_shots_missed
        global ai_shot_counter
        global row_letters
        global field_size

        used_letters = row_letters[:field_size]

        #print(f"\n-- current_ship: {current_ship} | Ships foundered: {ships_foundered_pl} | Amount of ships: {amount_of_ships} --")
        #print(f"-- ai_shots_missed: {ai_shots_missed} --")

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

            print(f"PREVSHELL: {ai_prev_shell}, RANDOM")


        # ---- FIRST POSITION FOUND, START FOCUS FIRING ---- #
        elif len(current_ship) >= 1:
            print(f"SHOTS: {ai_shot_counter}")

            # Fire left until a shot misses, should it exit the grid it will return to it's originial hit. #
            if ai_shot_counter <= 4:
                try:
                    newshot = ai_prev_shell[1][0] + str(int(ai_prev_shell[1][1]) - 1)
                    ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)
                    print(f"PREVSHELL: {ai_prev_shell[0]}, LEFT: {newshot}, Status: {ai_prev_shell[2]}")

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
                # Fire right until a shot misses, should it exit the grid it will return to it's originial hit. #
                if ai_shot_counter <= 8: # Fire right
                    try:
                        newshot = ai_prev_shell[1][0] + str(int(ai_prev_shell[1][1]) + 1)
                        ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)
                        print(f"PREVSHELL: {ai_prev_shell[0]}, RIGHT: {newshot}, Status: {ai_prev_shell[2]}")

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
                    # Fire upwards until a shot misses, should it exit the grid it will return to it's originial hit. #
                    if ai_shot_counter <= 12:  # Fire above
                        try:
                            top = used_letters[used_letters.index(ai_prev_shell[1][0]) - 1]
                            newshot = top + ai_prev_shell[1][1]
                            ai_prev_shell = self.fireAISequence(battlefield_pl, ship_positions_pl, newshot)
                            print(f"PREVSHELL: {ai_prev_shell[0]}, ABOVE: {newshot}, Status: {ai_prev_shell[2]}")

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
                                print(f"PREVSHELL: {ai_prev_shell[0]}, DOWN: {newshot}, Status: {ai_prev_shell[2]}")

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
        global ammo
        global ships_foundered_pl

        result = ['','','']
        result[1] = shot

        row, col = self.checkShellShot(battlefield_pl, shot)

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


    def insertText(self, dataname, battlefield):
        global ammo

        self.textdash.configure(state=NORMAL)
        self.textdash.insert(END, f"\nYou've got {ammo} rounds left!\n\n")

        for i in battlefield:
            self.textdash.insert(END, f"{i}\n")

        self.textdash.configure(state=DISABLED)
        self.jsonBattlefield({dataname : battlefield})


    def jsonBattlefield(self, item):
        with open('gui/AI/AIGame.json', 'r+') as file:
            data = json.load(file)
            data.update(item)
            file.seek(0)
            json.dump(data, file)
            file.close()


    def loadJson(self):
        global field_size
        global amount_of_ships
        global ammo

        with open('gui/AI/AIGame.json', 'r') as file:
            data = json.load(file)
            field_size = data['field_size']
            amount_of_ships = data['amount_of_ships']
            ammo = data['ammo']
            file.close()