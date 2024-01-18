from tkinter import *
from tkinter import messagebox


class TicTacToe:

    def aboutMe(self):
        """
        Placeholder function for About menu item.
        """
        messagebox.showinfo(
            "About", "Tic-Tac-Toe with Tkinter\nVersion 1.0\nCreated by [Your Name]")

    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        # Calculate an appropriate window size
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = min(screen_width, screen_height)
        window_height = window_width  # To make it a square window
        self.window.geometry(f"{window_width}x{window_height}")

        self.window.option_add("*Font", 'Times 16')
        self.window.configure(bg='#FFF8DC')
        self.window.resizable(False, False)
        self.moves = 0

        self.ImageX = PhotoImage(file="PythonX.png")
        self.ImageO = PhotoImage(file="PythonO.png")
        self.ImageBase = PhotoImage(file="PythonBase.png")
        self.ImageH = PhotoImage(file="PythonHorizontal2.png")
        self.ImageV = PhotoImage(file="PythonVertical.png")

        self.radioVar = IntVar()
        self.radio1 = Radiobutton(self.window, font=('Times', 25), text="X",
                                  variable=self.radioVar, value=1, command=self.select)
        self.radio2 = Radiobutton(self.window, font=('Times', 25), text="O",
                                  variable=self.radioVar, value=0, command=self.select)
        self.radio1.grid(row=2, column=4, sticky='W', pady=(50, 0))
        self.radio2.grid(row=2, column=5, sticky='W', pady=(50, 0))

        self.b11Val, self.b12Val, self.b13Val = 0, 0, 0
        self.b21Val, self.b22Val, self.b23Val = 0, 0, 0
        self.b31Val, self.b32Val, self.b33Val = 0, 0, 0

        self.create_grid()
        self.create_menu()

        self.window.mainloop()

    def create_grid(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = Button(self.window, image=self.ImageBase,
                                command=lambda r=row, c=col: self.cycle(r, c),
                                highlightthickness=0, bd=0)
                button.grid(row=row+2, column=col+1, sticky='W',
                            padx=(20, 0), pady=(50, 0))
                button_row.append(button)
            self.buttons.append(button_row)

    def cycle(self, row, col):
        button = self.buttons[row][col]
        if button["state"] == "normal":
            self.moves += 1
            if self.radioVar.get() == 1:
                button.configure(image=self.ImageX)
                self.set_board_value(row, col, 1)
                play = "X"
            else:
                button.configure(image=self.ImageO)
                self.set_board_value(row, col, -1)
                play = "O"
            button["state"] = "disabled"
            self.report(f"{play} played a move at Square ({row+1},{col+1})")

    def create_menu(self):
        # Create a menu bar
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.GameMenu = Menu(self.menubar, tearoff="off")
        self.menubar.add_cascade(label="Game", menu=self.GameMenu)
        self.AboutMenu = Menu(self.menubar, tearoff="off")
        self.menubar.add_cascade(label="About", menu=self.AboutMenu)

        # Add menu items to Game
        self.GameMenu.add_command(label="Play", background='#FAFAD2', activebackground='#FFFFFF',
                                  activeforeground='#FF0000', command=self.reset_game)
        self.GameMenu.add_command(
            label="Quit", background='#FAFAD2', command=self.window.destroy)
        self.GameMenu.add_command(
            label="Exit", background='#FFE4E1', command=self.window.quit)

        # Add menu items to About
        self.AboutMenu.add_command(label="About Me", command=self.aboutMe)
        self.window.config(menu=self.menubar)

    def select(self):
        """
        Handle the radio button selection.
        """
        # Check if a winner has already been found
        if self.check_winner():
            return

        # Process the radio button selection
        if self.radioVar.get() == 1:
            self.play_move("X")
        else:
            self.play_move("O")

    def play_move(self, player):
        """
        Handle a player's move on the board.
        """
        # Ensure that the player has not already moved in this cell
        if not self.is_cell_empty(player):
            return

        # Get the current cell and update its value
        current_cell = self.get_current_cell()
        if current_cell:
            current_cell.configure(
                image=self.ImageX if player == "X" else self.ImageO)
            self.moves += 1

        # Check for a winner and update the report
        self.report(
            f"{player} played a move at Square {self.get_current_position()}")

    def get_current_cell(self):
        """
        Get the current cell based on the radio button selection.
        """
        if self.radioVar.get() == 1:
            if self.b11Val == 0:
                return self.b11
            elif self.b12Val == 0:
                return self.b12
            elif self.b13Val == 0:
                return self.b13
        elif self.radioVar.get() == 0:
            if self.b11Val == 0:
                return self.b11
            elif self.b12Val == 0:
                return self.b12
            elif self.b13Val == 0:
                return self.b13

        return None

    def get_current_position(self):
        """
        Get the position of the current cell based on the radio button selection.
        """
        if self.radioVar.get() == 1:
            if self.b11Val == 0:
                return "(1,1)"
            elif self.b12Val == 0:
                return "(1,2)"
            elif self.b13Val == 0:
                return "(1,3)"
        elif self.radioVar.get() == 0:
            if self.b11Val == 0:
                return "(1,1)"
            elif self.b12Val == 0:
                return "(1,2)"
            elif self.b13Val == 0:
                return "(1,3)"

        return None

    def is_cell_empty(self, player):
        """
        Check if the current cell is empty for the given player.
        """
        if self.radioVar.get() == 1:
            if player == "X":
                return self.b11Val == 0
            elif player == "O":
                return self.b11Val == 0
        elif self.radioVar.get() == 0:
            if player == "X":
                return self.b11Val == 0
            elif player == "O":
                return self.b11Val == 0

        return False

    def cycle11(self):
        """
        Handle the button click event for the cell (1,1).
        """
        self.moves += 1
        if self.radioVar.get() == 1:
            self.b11.configure(image=self.ImageX)
            self.b11Val = 1
            play = "X"
        else:
            self.b11.configure(image=self.ImageO)
            self.b11Val = -1
            play = "O"
        self.b11["state"] = "disabled"
        self.report(f"{play} played a move at Square (1,1)")

    # Implement cycle12, cycle13, cycle21, cycle22, cycle23, cycle31, cycle32, and cycle33 similarly

    def check_winner(self):
        """
        Check if there is a winner on the board.
        """
        hch1 = self.b11Val + self.b12Val + self.b13Val
        # ... Implement the rest of the combinations ...
        hch1 = self.b11Val + self.b12Val + self.b13Val
        hch2 = self.b21Val + self.b22Val + self.b23Val
        hch3 = self.b31Val + self.b32Val + self.b33Val
        vch1 = self.b11Val + self.b21Val + self.b31Val
        vch2 = self.b12Val + self.b22Val + self.b32Val
        vch3 = self.b13Val + self.b23Val + self.b33Val
        dch1 = self.b11Val + self.b22Val + self.b33Val
        dch2 = self.b13Val + self.b22Val + self.b31Val

        winnerX = hch1 == 3 or hch2 == 3 or hch3 == 3 or vch1 == 3 or vch2 == 3 or vch3 == 3 or dch1 == 3 or dch2 == 3
        winnerO = hch1 == -3 or hch2 == -3 or hch3 == -3 or vch1 == - \
            3 or vch2 == -3 or vch3 == -3 or dch1 == -3 or dch2 == -3

        # The rest of the code...
        # ...

        if winnerX:
            self.winner = "X"
            self.disable_board()
            self.disable_radio_buttons()  # Disable radio buttons when there's a winner
            return True
        elif winnerO:
            self.winner = "O"
            self.disable_board()
            self.disable_radio_buttons()  # Disable radio buttons when there's a winner
            return True
        else:
            if self.moves == 9:
                print("There is a tie.")
                # Write code to add Label to the GUI window that there is a tie
            else:
                return False

    def report(self, moveInfo):
        """
        Print the move information to the console and check for a winner.
        """
        print(moveInfo)
        if self.check_winner():
            print(f"{self.winner} has won the game")  # Output to Console
        else:
            print("No winner yet")

    def disable_radio_buttons(self):
        """
        Disable the radio buttons.
        """
        self.radio1["state"] = "disabled"
        self.radio2["state"] = "disabled"

    def enable_radio_buttons(self):
        """
        Enable the radio buttons.
        """
        self.radio1["state"] = "normal"
        self.radio2["state"] = "normal"

    def reset_game(self):
        """
        Reset the game board for a new game.
        """
        # Reset the button states and values
        self.b11.configure(image=self.ImageBase, state='normal')
        self.b12.configure(image=self.ImageBase, state='normal')
        self.b13.configure(image=self.ImageBase, state='normal')
        self.b21.configure(image=self.ImageBase, state='normal')
        self.b22.configure(image=self.ImageBase, state='normal')
        self.b23.configure(image=self.ImageBase, state='normal')
        self.b31.configure(image=self.ImageBase, state='normal')
        self.b32.configure(image=self.ImageBase, state='normal')
        self.b33.configure(image=self.ImageBase, state='normal')

        # Reset the values
        self.b11Val, self.b12Val, self.b13Val = 0, 0, 0
        self.b21Val, self.b22Val, self.b23Val = 0, 0, 0
        self.b31Val, self.b32Val, self.b33Val = 0, 0, 0

        # Reset the moves count
        self.moves = 0

        # Enable radio buttons
        self.radio1["state"] = "normal"
        self.radio2["state"] = "normal"

        self.enable_radio_buttons()


# Entry point for the game
if __name__ == "__main__":
    game = TicTacToe()
