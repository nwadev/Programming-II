# Chukwueemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2

from tkinter import *
from tkinter import messagebox


class TicTacToe:

    def aboutMe(self):
        messagebox.showinfo(
            "About", "Could'nt figure out how to use the PythonHorizontal2.png and PythonVertical.png images properly :( ")

    # Create the main window

    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.option_add("*Font", 'Times 16')
        self.window.configure(bg='#FFF8DC')
        self.window.geometry("1200x1600")
        self.moves = 0
        self.game_over = False

        # Load images for X, O, and base grid
        self.ImageX = PhotoImage(file="PythonX.png")
        self.ImageO = PhotoImage(file="PythonO.png")
        self.ImageBase = PhotoImage(file="PythonBase.png")
        self.ImageH = PhotoImage(file="PythonHorizontal2.png")
        self.ImageV = PhotoImage(file="PythonVertical.png")

        # Create and place title label
        self.label_title = Label(self.window, text='Tic - Tac - Toe',
                                 font=('Times 18 bold'), bg='#FFF8DC', fg='#D2691E')
        self.label_title.grid(row=0, column=1, padx=20, pady=(
            5, 20), sticky='NSEW', columnspan=3)

        self.buttons = []

        # Adjust column weights to stretch the widgets
        for row in range(3):
            for col in range(3):
                button = Button(self.window, image=self.ImageBase,
                                command=lambda r=row, c=col: self.cycle(r, c),
                                highlightthickness=0, bd=0)
                button.grid(row=row+1, column=col+1, sticky='NSEW', ipadx=.5,
                            ipady=.5, padx=5, pady=5)
                self.buttons.append(button)

        for i in range(5):
            self.window.columnconfigure(i, weight=1)
            self.window.rowconfigure(0, weight=1)
            self.window.rowconfigure(4, weight=1)

        self.radioVar = IntVar()
        self.radio1 = Radiobutton(self.window, font=(
            'Times', 25), text="X", variable=self.radioVar, value=1, command=self.select)
        self.radio2 = Radiobutton(self.window, font=(
            'Times', 25), text="O", variable=self.radioVar, value=0, command=self.select)
        self.radio1.grid(row=1, column=4, sticky='N', pady=5)
        self.radio2.grid(row=1, column=5, sticky='N', pady=5)

        # Add a label to display the winner
        self.winner_label = Label(self.window, text="", font=(
            'Times 18 bold'), bg='#FFF8DC', fg='#D2691E')
        self.winner_label.grid(
            row=1, column=4, pady=(15, 0), sticky='W')

        vbar1 = Label(self.window, image=self.ImageV,
                      highlightthickness=0, bd=0)
        vbar1.grid(row=1, column=2, sticky='W', rowspan=6,
                   ipadx=0, ipady=0, pady=(0, 0))

        vbar2 = Label(self.window, image=self.ImageV,
                      highlightthickness=0, bd=0)
        vbar2.grid(row=1, column=3, sticky='W', rowspan=6,
                   ipadx=0, ipady=0, pady=(0, 0))

        hbar1 = Label(self.window, image=self.ImageH,
                      highlightthickness=0, bd=0)
        hbar1.grid(row=1, column=0, sticky='W', columnspan=6,
                   ipadx=0, ipady=0, padx=(10, 0))
        hbar2 = Label(self.window, image=self.ImageH,
                      highlightthickness=0, bd=0)
        hbar2.grid(row=2, column=0, sticky='W', columnspan=6,
                   ipadx=0, ipady=0, padx=(10, 0))

        hbar1.place(x=50, y=380)
        hbar2.place(x=50, y=695)

        self.create_menu()
        self.window.mainloop()

    def display_winner_message(self, winner):
        "Updates the winner_label with the winner message."
        self.winner_label.config(text=f"{winner} has won the game")

    def cycle(self, row, col):
        if not self.game_over:
            # Get button from grid
            button = self.buttons[row * 3 + col]
            if button["state"] == "normal":
                self.moves += 1
                if self.radioVar.get() == 1:
                    # Set X image
                    button.configure(image=self.ImageX)
                    # Store board value
                    self.set_board_value(row, col, 1)
                    play = "X"
                    # Report move
                    self.report(
                        f"{play} played a move at Square ({row+1},{col+1})")
                else:
                    button.configure(image=self.ImageO)
                    self.set_board_value(row, col, -1)
                    play = "O"
                button["state"] = "disabled"
                self.report(
                    f"{play} played a move at Square ({row+1},{col+1})")

                # Check for a winner
                if self.check_winner():
                    self.game_over = True
                    self.disableBoard()
                    self.display_winner_message(
                        self.winner)  # Display winner message
                else:
                    # Display tie message
                    if self.moves == 9:
                        self.winner_label.config(text="It's a tie!")
                        self.game_over = True

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
                                  activeforeground='#FF0000')
        self.GameMenu.add_command(
            label="Quit", background='#FAFAD2', command=self.window.destroy)
        self.GameMenu.add_command(
            label="Exit", background='#FFE4E1', command=self.window.quit)

        # Add menu items to About
        self.AboutMenu.add_command(label="About Me", command=self.aboutMe)
        self.window.config(menu=self.menubar)
        self.AboutMenu.add_command(
            label="EasterEGG", background='#FAFAD2')

    def set_board_value(self, row, col, value):
        # First row
        if row == 0:
            if col == 0:
                self.b11Val = value
            elif col == 1:
                self.b12Val = value
            elif col == 2:
                self.b13Val = value
        # Second row
        elif row == 1:
            if col == 0:
                self.b21Val = value
            elif col == 1:
                self.b22Val = value
            elif col == 2:
                self.b23Val = value
        # Third row
        elif row == 2:
            if col == 0:
                self.b31Val = value
            elif col == 1:
                self.b32Val = value
            elif col == 2:
                self.b33Val = value

    # check for winner
    def check_winner(self):
        # Checkin rows
        hch1 = self.b11Val + self.b12Val + self.b13Val
        hch2 = self.b21Val + self.b22Val + self.b23Val
        hch3 = self.b31Val + self.b32Val + self.b33Val
        # Checkin columns
        vch1 = self.b11Val + self.b21Val + self.b31Val
        vch2 = self.b12Val + self.b22Val + self.b32Val
        vch3 = self.b13Val + self.b23Val + self.b33Val
        # Checkin diagonals
        dch1 = self.b11Val + self.b22Val + self.b33Val
        dch2 = self.b13Val + self.b22Val + self.b31Val

        winnerX = hch1 == 3 or hch2 == 3 or hch3 == 3 or vch1 == 3 or vch2 == 3 or vch3 == 3 or dch1 == 3 or dch2 == 3
        winnerO = hch1 == -3 or hch2 == -3 or hch3 == -3 or vch1 == - \
            3 or vch2 == -3 or vch3 == -3 or dch1 == -3 or dch2 == -3

        if winnerX:
            self.winner = "X"
            return True
        elif winnerO:
            self.winner = "O"
            return True
        else:
            return False

    # Print move info

    def report(self, moveInfo):
        print(moveInfo)
        if self.check_winner():
            print(f"{self.winner} has won the game")
        else:
            print("No winner yet")

    # Disable all buttons

    def disableBoard(self):
        for button in self.buttons:
            button["state"] = "disabled"

    def select(self):
        pass


# Create an instance of the TicTacToe class to start the game
TicTacToe()
if __name__ == "__main__":
    game = TicTacToe()
