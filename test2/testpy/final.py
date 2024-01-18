from tkinter import *


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("1200x1600")
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

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = Button(self.window, image=self.ImageBase,
                                command=lambda r=row, c=col: self.cycle(r, c),
                                highlightthickness=0, bd=0)
                button.grid(row=row+1, column=col+1, sticky='W', ipadx=0,
                            ipady=0, padx=(20, 0), pady=(50, 0))
                button_row.append(button)
            self.buttons.append(button_row)

        self.radioVar = IntVar()
        self.radio1 = Radiobutton(self.window, font=(
            'Times', 25), text="X", variable=self.radioVar, value=1, command=self.select)
        self.radio2 = Radiobutton(self.window, font=(
            'Times', 25), text="O", variable=self.radioVar, value=0, command=self.select)
        self.radio1.grid(row=1, column=4, sticky='N', pady=(50, 0))
        self.radio2.grid(row=1, column=5, sticky='N', pady=(50, 0))

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
        hbar2.place(x=0, y=750)
        hbar1.place(x=0, y=400)

        self.window.mainloop()

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

    def set_board_value(self, row, col, value):
        if row == 0:
            if col == 0:
                self.b11Val = value
            elif col == 1:
                self.b12Val = value
            elif col == 2:
                self.b13Val = value
        elif row == 1:
            if col == 0:
                self.b21Val = value
            elif col == 1:
                self.b22Val = value
            elif col == 2:
                self.b23Val = value
        elif row == 2:
            if col == 0:
                self.b31Val = value
            elif col == 1:
                self.b32Val = value
            elif col == 2:
                self.b33Val = value

    def check_winner(self):
        # The check_winner logic remains the same as before.
        # Implement it here...

        def report(self, moveInfo):
            print(moveInfo)
        if self.check_winner():
            print(f"{self.winner} has won the game")
        else:
            print("No winner yet")

    def disableBoard(self):
        for row in self.buttons:
            for button in row:
                button["state"] = "disabled"

    def select(self):
        pass


# Create an instance of the TicTacToe class to start the game
TicTacToe()
