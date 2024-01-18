from tkinter import *


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        # Set the initial window size (800x800)
        self.window.geometry("800x800")

        # Allow the window to be resized both horizontally and vertically
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.window.option_add("*Font", 'Times 14')  # Decrease font size
        self.window.configure(bg='#FFF8DC')
        self.moves = 0
        self.winner = None

        self.ImageX = PhotoImage(file="PythonX.png").subsample(
            2)  # Reduce image size
        self.ImageO = PhotoImage(file="PythonO.png").subsample(
            2)  # Reduce image size
        self.ImageBase = PhotoImage(
            file="PythonBase.png").subsample(2)  # Reduce image size
        self.ImageH = PhotoImage(file="PythonHorizontal2.png").subsample(
            2)  # Reduce image size
        self.ImageV = PhotoImage(file="PythonVertical.png").subsample(
            2)  # Reduce image size

        self.board = [[0 for _ in range(3)] for _ in range(3)]

        self.label_title = Label(self.window, text='Tic - Tac - Toe',
                                 font=('Times 18 bold'), bg='#FFF8DC', fg='#D2691E')
        self.label_title.grid(row=0, column=0, padx=(
            20, 0), pady=(5, 0), sticky='EW', columnspan=3)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = Button(self.window, image=self.ImageBase,
                                                command=lambda r=row, c=col: self.on_click(r, c), highlightthickness=0, bd=0)
                self.buttons[row][col].grid(
                    row=row+1, column=col, padx=(20, 0), pady=(50, 0), sticky='NSEW')

        # Set uniform weights for rows and columns
        for i in range(1, 4):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

        self.window.mainloop()

    def on_click(self, row, col):
        if self.board[row][col] == 0 and self.winner is None:
            self.moves += 1
            player = self.radioVar.get()  # 1 for X, 0 for O
            if player == 1:
                self.buttons[row][col].configure(image=self.ImageX)
                self.board[row][col] = 1
            else:
                self.buttons[row][col].configure(image=self.ImageO)
                self.board[row][col] = -1

            if self.check_winner():
                self.report(f"Player {player} has won the game")
            else:
                if self.moves == 9:
                    self.report("There is a tie.")
                else:
                    self.report(
                        f"Player {player} played a move at Square ({row+1},{col+1})")

    def check_winner(self):
        for i in range(3):
            if abs(sum(self.board[i])) == 3 or abs(sum(self.board[j][i] for j in range(3))) == 3:
                self.winner = 1 if sum(self.board[i]) == 3 else 0
                self.disable_board()
                return True
        if abs(self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3 or abs(self.board[0][2] + self.board[1][1] + self.board[2][0]) == 3:
            self.winner = 1 if self.board[1][1] == 1 else 0
            self.disable_board()
            return True
        return False

    def report(self, move_info):
        print(move_info)

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"


# Create an instance of the TicTacToe class to start the game
TicTacToe()
