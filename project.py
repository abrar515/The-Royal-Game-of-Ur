from os import system as _cmd
from os import name as _osname
from random import randint
from tabulate import tabulate
import time

#########################TESTMODE############################
#Keep False for normal gameplay
test_mode = False
#############################################################

PLAYER_1 = "⬜️"
PLAYER_1_SYMBOLS = ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"]
#PLAYER_1_SYMBOLS = ["🟥","🟧"]

PLAYER_2 = "⚪️"
PLAYER_2_SYMBOLS = ["🔴","🟠","🟡","🟢","🔵","🟣","🟤"]
#PLAYER_2_SYMBOLS = ["🔴","🟠"]

ROSETTES = {4, 8, 14}

def clear_screen():
    try:
        _cmd('cls' if _osname == 'nt' else 'clear')
    except Exception:
        pass
class Board:
    def __init__(self):
        self.empty = "  "

        self.layout = {
        "A0" : self.empty, "A1" : self.empty, "A2" : self.empty, "A3" : self.empty, "A4" : self.empty,
        "B0" : self.empty, "B1" : self.empty, "B2" : self.empty, "B3" : self.empty, "B4" : self.empty,
        "5" : self.empty, "6" : self.empty, "7" : self.empty, "8" : self.empty, "9" : self.empty, "10" : self.empty, "11" : self.empty, "12" : self.empty,
        "A13" : self.empty, "A14" : self.empty, "A15" : self.empty,
        "B13" : self.empty, "B14" : self.empty, "B15" : self.empty
        }

    def board_print(self):
        #rosette cell design
        r_tb = Yellow("+---+")
        r = Yellow("│")

        return f"""
╔═══════╦═══════╦═══════╦═══════╗               ╔═══════╦═══════╗
║ {r_tb} ║       ║       ║       ║               ║ {r_tb} ║       ║
║ {r}{self.layout["A4"]} {r} ║  {self.layout["A3"]}   ║  {self.layout["A2"]}   ║  {self.layout["A1"]}   ║               ║ {r}{self.layout["A14"]} {r} ║  {self.layout["A13"]}   ║
║ {r_tb} ║       ║       ║       ║               ║ {r_tb} ║       ║
╠═══════╬═══════╬═══════╬═══════╬═══════╦═══════╬═══════╣═══════╣
║       ║       ║       ║ {r_tb} ║       ║       ║       ║       ║
║  {self.layout["5"]}   ║  {self.layout["6"]}   ║  {self.layout["7"]}   ║ {r}{self.layout["8"]} {r} ║  {self.layout["9"]}   ║  {self.layout["10"]}   ║  {self.layout["11"]}   ║  {self.layout["12"]}   ║
║       ║       ║       ║ {r_tb} ║       ║       ║       ║       ║
╠═══════╬═══════╬═══════╬═══════╣═══════╩═══════╬═══════╬═══════╣
║ {r_tb} ║       ║       ║       ║               ║ {r_tb} ║       ║
║ {r}{self.layout["B4"]} {r} ║  {self.layout["B3"]}   ║  {self.layout["B2"]}   ║  {self.layout["B1"]}   ║               ║ {r}{self.layout["B14"]} {r} ║  {self.layout["B13"]}   ║
║ {r_tb} ║       ║       ║       ║               ║ {r_tb} ║       ║
╚═══════╩═══════╩═══════╩═══════╝               ╚═══════╩═══════╝
"""

    def show_board(self, show_pieces, player):

        #if the pieces are needed to be shown
        if show_pieces == True:
            if player == PLAYER_1:
                keys = [item[0] for item in self._dict_player_1.items()]
                values = [item[1].symbol for item in self._dict_player_1.items()]
                table = [keys, values]
                table_pieces = f'Pieces:\n{tabulate(table, headers="firstrow", tablefmt="rounded_outline", stralign="center")}\n'
            elif player == PLAYER_2:
                keys = [item[0] for item in self._dict_player_2.items()]
                values = [item[1].symbol for item in self._dict_player_2.items()]
                table = [keys, values]
                table_pieces = f'Pieces:\n{tabulate(table, headers="firstrow", tablefmt="rounded_outline", stralign="center")}\n'

        #if the pieces are not needed to be shown
        else:
            table_pieces = "\n\n\n\n\n\n"

        #rosette cell design
        r_tb = Yellow("+---+")
        r = Yellow("│")
        clear_screen()
        return f"""
{Green("────────────────────────────────────────────────────────────────────")}
{Green("─                       THE ROYAL GAME OF UR                       ─")}
{Green("────────────────────────────────────────────────────────────────────")}

Board:
{self.board_print()}

{table_pieces}
{Green("────────────────────────────────────────────────────────────────────")}
        """

    def add_pieces(self):
        self._dict_player_1 = {}
        self._dict_player_2 = {}

        for _index, symbol in enumerate(PLAYER_1_SYMBOLS, 1):
            self._dict_player_1[_index] = Piece(PLAYER_1, symbol, _index)

        for _index, symbol in enumerate(PLAYER_2_SYMBOLS, 1):
            self._dict_player_2[_index] = Piece(PLAYER_2, symbol, _index)


    def show_paths(self):
        r_tb = Yellow("+---+")
        r = Yellow("│")
        clear_screen()
        return f"""
{Green("────────────────────────────────────────────────────────────────────")}
{Green("─                       THE ROYAL GAME OF UR                       ─")}
{Green("────────────────────────────────────────────────────────────────────")}

{Yellow("Board:")}
╔═══════╦═══════╦═══════╦═══════╗               ╔═══════╦═══════╗
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╠═══════╬═══════╬═══════╬═══════╬═══════╦═══════╬═══════╣═══════╣
║       ║       ║       ║ +---+ ║       ║       ║       ║       ║
║   ┌───┼───────┼───────┼─┼───┼─┼───────┼───────┼───────┼────┐  ║
║   │   ║       ║       ║ +---+ ║       ║       ║       ║    │  ║
╠═══┼═══╬═══════╬═══════╬═══════╣═══════╩═══════╬═══════╬════┼══╣
║ +-│-+ ║       ║       ║       ║               ║ +---+ ║    │  ║
║ │ └─┼─┼───────┼───────┼───────┼{Yellow("◄─START")}   {Green("END ◄")}┼─┼───┼─┼────┘  ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╚═══════╩═══════╩═══════╩═══════╝               ╚═══════╩═══════╝
        """

    def roll_dice(self):
        for j in range(10):
            dice = ""
            #dice = [randint(0, 1) for _ in range(4)]
            for i in range(4):
                roll = randint(0, 1)
                if roll == 0:
                    dice += "   △"
                else:
                    dice += "   ⛰"
            clear_screen()
            print(f"""
{Green("────────────────────────────────────────────────────────────────────")}
{Green("─                       THE ROYAL GAME OF UR                       ─")}
{Green("────────────────────────────────────────────────────────────────────")}

Board:
{self.board_print()}
\n\n
{dice}  {('  =  ' + str(dice.count('⛰'))) if j == 9 else ''}
\n\n\n
{Green("────────────────────────────────────────────────────────────────────")}
        """)
            time.sleep(.1)

        time.sleep(1)
        return dice.count('⛰')


    def __str__(self):
        ...



class Piece:
    def __init__(self, player, symbol, number):
        self.player = player
        self.number = number
        if self.player == PLAYER_1:
            self.path = ["B0", "B1", "B2", "B3", "B4", "5", "6", "7", "8", "9", "10", "11", "12", "B13", "B14", "B15"]
        else:
            self.path = ["A0", "A1", "A2", "A3", "A4", "5", "6", "7", "8", "9", "10", "11", "12", "A13", "A14", "A15"]

        self.position = 0
        self.symbol = symbol
        self.won = False


    def move(self, steps, board):

        start_pos = self.position
        target_pos = start_pos + steps

        #Overflow (cannot move beyond finish)
        if target_pos >= len(self.path):
            raise Exception(Red(f"Too many steps!  Can't move the chosen piece by {steps} steps"))

        start_cell = self.path[start_pos]
        target_cell = self.path[target_pos]


        #if the piece is winning
        if target_pos == len(self.path)-1:
            board.layout[start_cell] = board.empty
            board.layout[target_cell] = board.empty
            self.position = target_pos
            self.won = True
            #create a reference to the dict of pieces of the current player
            pieces = board._dict_player_1 if self.player == PLAYER_1 else board._dict_player_2
            pieces.pop(self.number)
            return Cyan(f"{self.player} has scored one piece"), board.layout

        #if target cell is empty
        elif board.layout[target_cell] == board.empty:
            board.layout[target_cell] = self
            board.layout[start_cell] = board.empty
            self.position = target_pos
            return Green(f"The chosen piece has been moved by {steps} steps"), board.layout


        #if enemy's piece is on rosette (Safe cell)

        elif isinstance(board.layout[target_cell], Piece):

            #if the piece can't be moved because of another piece in the target cell
            if board.layout[target_cell].player == self.player:
                raise Exception(Red("Can't move the chosen piece! You already have a piece there."))

            #if the piece can't be moved because of enemy piece in the target rosette cell
            elif target_pos in ROSETTES:
                return Red(f"Can't move because enemy's piece is on the safe place"), board.layout

            #if piece is to be moved while taking out the enemy's piece
            else:
                board.layout[target_cell].position = 0
                board.layout[target_cell] = self
                board.layout[start_cell] = board.empty
                self.position = target_pos
                return Cyan(f"Enemy's piece taken out"), board.layout

        raise Exception(Red("Something is wrong with the target cell!"))




    def showposition(self):
        return self.path[self.position]



    def __str__(self):
        return f"{self.symbol}"


def main():

    game_end = False
    roll_again = False
    #Set turn for player PLAYER_1
    player = PLAYER_1

    board = Board()
    board.add_pieces()

    #INTRO
    selection = intro_screen(board)


    while game_end == False:
        message = ""
        if roll_again == False:
            print(board.show_board(False, player))
            print(f"It is the turn of {player}  player")
            print()

        input(Yellow("Press enter to roll the dice"))

        if test_mode == False:
            n = board.roll_dice()
        else:
            n = int(input(f"player = {player} | choose steps: "))

        movement = can_move(n, player, board)
        roll_again = False

        if not (n == 0 or movement == False):
            print(board.show_board(True, player))

        while True:
            try:

                #if dice roll gives zero
                if n == 0:
                    print(board.show_board(False, player))
                    print(message)
                    print(Red("You got ZERO on dice!"))
                    input(f"{Yellow('Press enter to pass to the next player.')}")
                    player = change_player(player)
                    break


                #if none of the pieces can be moved by the steps given by dice roll
                if movement == False:
                    print(board.show_board(False, player))
                    print(message)
                    print(Red(f"Can't move any piece by {n} steps"))
                    input(f"{Yellow('Press enter to pass to the next player.')}")
                    player = change_player(player)
                    break


                #if the player can move at least one piece
                print(Green(f"You can move a piece by {n} steps."))
                print(message)
                chosen_piece = int(input(Yellow("Choose a piece to move: ")))  # when choosing a piece that can't move to end and will move too many steps, the loop should continue appropriately
                active_piece = choose_piece(chosen_piece, player, board)   ##can combine this and the following line and make it part of the class Piece
                message, board.layout = active_piece.move(n, board)

                #if the player just scored the last piece and won
                if len(board._dict_player_1) == 0:
                    print("Player 1 has won!")
                    game_end = True
                    break
                elif len(board._dict_player_2) == 0:
                    print("Player 2 has won!")
                    game_end = True
                    break


                #if the piece lands on a safe cell (rosette)
                if active_piece.position in ROSETTES:
                    print(board.show_board(False, player))
                    print(message)
                    print(Cyan("✧✧✧✧✧✧ You get to roll the dice again! ✧✧✧✧✧✧"))
                    roll_again = True
                    break

                #if the piece moves to other than safe cells
                else:
                    print(board.show_board(False, player))
                    print()
                    print(message)
                    input(f"{Yellow('Press enter to pass to the next player.')}")
                    player = change_player(player)
                    break


            #if the player enters a non-integer
            except ValueError:
                print(board.show_board(True, player))
                message = Red("Enter a number referring to one of the pieces")

            #if the player enters an integer not referring to any piece
            except KeyError:
                print(board.show_board(True, player))
                message = Red("Choose a vaid piece")

            #if the chosen piece cannot move because of an enemy piece on safe cell or the steps are too many for the board
            except Exception as e:
                print(board.show_board(True, player))
                message = e





def change_player(player):
    return PLAYER_2 if player == PLAYER_1 else PLAYER_1


def choose_piece(chosen_piece, player, board):
    return (board._dict_player_1 if player == PLAYER_1 else board._dict_player_2)[chosen_piece]

def can_move(steps, player, board):
    #create a reference to the dict of pieces of the current player
    pieces = board._dict_player_1 if player == PLAYER_1 else board._dict_player_2

    for _, piece in pieces.items():
        target_pos = piece.position + steps

        #check if steps lead to out of path
        if target_pos >= len(piece.path):
            continue

        target_cell = board.layout[piece.path[target_pos]]

        #check if steps lead to empty cell
        if target_cell == board.empty:
            return True

        #check if steps lead to occupied cell
        elif isinstance(target_cell, Piece):
            if target_cell.player == player:
                continue
            elif target_pos in ROSETTES:
                continue

        #last condition (occupied by enemy and not a rosette)
        else:
            return True
    #if no True move detected in the for loop
    return False


def intro_screen(board):
    menu = True
    while menu == True:
        clear_screen()
        print(f"""
    ┌────────────────────────────────────────────────────────────────────────────┐
    │                                                                            │
    │                     {Green("WELCOME TO THE ROYAL GAME OF UR")}                        │
    │   ╔═══════╦═══════╦═══════╦═══════╗               ╔═══════╦═══════╗        │
    │   ║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║        │
    │   ║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║        │
    │   ║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║        │
    │   ╠═══════╬═══════╬═══════╬═══════╬═══════╦═══════╬═══════╣═══════╣        │
    │   ║       ║       ║       ║ +---+ ║       ║       ║       ║       ║        │
    │   ║       ║       ║       ║ │   │ ║       ║       ║       ║       ║        │
    │   ║       ║       ║       ║ +---+ ║       ║       ║       ║       ║        │
    │   ╠═══════╬═══════╬═══════╬═══════╬═══════╩═══════╬═══════╣═══════╣        │
    │   ║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║        │
    │   ║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║        │
    │   ║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║        │
    │   ╚═══════╩═══════╩═══════╩═══════╝               ╚═══════╩═══════╝        │
    │                                                                            │
    │   {Green("Menu:")}                                                                    │
    │            {Yellow("1   Start Game")}                                                  │
    │            {Yellow("2   Rules")}                                                       │
    │            {Yellow("3   Quit")}                                                        │
    │                                                                            │
    │                                                                            │
    └────────────────────────────────────────────────────────────────────────────┘
        """)
        selection = input(Yellow("Enter the a number from the menu and press enter...   "))
        if "1" in selection and not(("2" or "3") in selection):
            break
        elif "2" in selection and not(("1" or "3") in selection):
            print(board.show_paths())
            print(f"""{Yellow("Rosette cell:            Normal Cell:")}
        ╔═══════╗               ╔═══════╗
        ║ +---+ ║               ║       ║
        ║ │   │ ║               ║       ║
        ║ +---+ ║               ║       ║
        ╚═══════╝               ╚═══════╝
The Royal Game of Ur is a 2 player game.

{Yellow("🎯 Objective:")}
Move all of your pieces from START to END before your opponent.

{Yellow("🎲 Dice:")}
Four binary dice (each gives 0 or 1). The total number of 1s determines
how many squares you move a chosen piece.

{Yellow("⬜️ Movement:")}
• You may move any of your pieces that can legally advance by the dice roll.
• Pieces start off the board and enter from START position at the player side.
• Pieces move along their specific track, share the center path,
  and then exit toward their home squares.

{Yellow("⚔️ Capturing:")}
• Landing on an opponent’s piece sends it back off the board.
• You cannot capture if the opponent is on a Rosette.

{Yellow("⭐ Rosettes (Safe Cells):")}
• Landing on a Rosette gives you an extra roll.
• Pieces on Rosettes cannot be captured.
{Green("────────────────────────────────────────────────────────────────────────────")}
Tip: Think carefully—sometimes holding back is safer than charging ahead!
{Green("────────────────────────────────────────────────────────────────────────────")}
""")
            input(Yellow("Press enter to go back to menu...    "))
            pass
        elif "3" in selection and not(("1" or "2") in selection):
            clear_screen()
            quit()
    clear_screen()


def Red(s): return "\033[91m{}\033[00m".format(s)
def Green(s): return "\033[92m{}\033[00m".format(s)
def Yellow(s): return "\033[93m{}\033[00m".format(s)
def LightPurple(s): return "\033[94m{}\033[00m".format(s)
def Purple(s): return "\033[95m{}\033[00m".format(s)
def Cyan(s): return "\033[96m{}\033[00m".format(s)
def LightGray(s): return "\033[97m{}\033[00m".format(s)
def Black(s): return "\033[90m{}\033[00m".format(s)

if __name__ == "__main__":
    main()
