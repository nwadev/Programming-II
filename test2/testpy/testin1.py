from tkinter import *


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("600x600")
        self.window.option_add("*Font", 'Times 16')
        self.window.configure(bg='#FFF8DC')
        self.window.resizable(False, False)
        self.moves = 0

        self.ImageX = PhotoImage(file="PythonX.png")
        self.ImageO = PhotoImage(file="PythonO.png")
        self.ImageBase = PhotoImage(file="PythonBase.png")
        self.ImageH = PhotoImage(file="PythonHorizontal2.png")
        self.ImageV = PhotoImage(file="PythonVertical.png")

        self.label_title = Label(self.window, text='Tic - Tac - Toe',
                                 font=('Times 18 bold'), bg='#FFF8DC', fg='#D2691E')
        self.label_title.grid(row=0, column=1, padx=(
            20, 0), pady=(5, 0), sticky='WS', columnspan=7)

        self.b11Val, self.b12Val, self.b13Val = 0, 0, 0
        self.b21Val, self.b22Val, self.b23Val = 0, 0, 0
        self.b31Val, self.b32Val, self.b33Val = 0, 0, 0

        self.b11 = Button(self.window, image=self.ImageBase,
                          command=self.cycle11, highlightthickness=0, bd=0)
        self.b11.grid(row=1, column=1, sticky='W', ipadx=0,
                      ipady=0, padx=(20, 0), pady=(50, 0))

        self.radioVar = IntVar()
        self.radio1 = Radiobutton(self.window, font=(
            'Times', 25), text="X", variable=self.radioVar, value=1, command=self.select)
        self.radio2 = Radiobutton(self.window, font=(
            'Times', 25), text="O", variable=self.radioVar, value=0, command=self.select)
        self.radio1.grid(row=1, column=6, sticky='N', pady=(50, 0))
        self.radio2.grid(row=1, column=7, sticky='N', pady=(50, 0))

        self.window.mainloop()

    def cycle11(self):
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

    # Define cycle12, cycle13, ..., cycle33 functions in a similar manner.

    def check_winner(self):
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

        if winnerX:
            self.winner = "X"
            self.disableBoard()
            return True
        elif winnerO:
            self.winner = "O"
            self.disableBoard()
            return True
        else:
            if self.moves == 9:
                print("There is a tie.")
                # write code to add Label to the GUI window that there is a tie
            else:
                return False

    def report(self, moveInfo):
        print(moveInfo)
        if self.check_winner():
            print(f"{self.winner} has won the game")  # Output to Console
        else:
            print("No winner yet")

    def disableBoard(self):
        self.b11["state"] = "disabled"
        # Add similar code to disable other buttons (b12, b13, ..., b33)

    # Add missing 'select' function
    def select(self):
        pass


# Create an instance of the TicTacToe class to start the game
TicTacToe()
