import tkinter as tk
from tkinter import ttk


class PalindromeCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chukwu's Palindrome Checker")

        self.setup_ui()

    def setup_ui(self):
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Times New Roman', 14))
        self.style.configure('TLabel', font=('Times New Roman', 14))

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.grid(row=0, column=0)

        ttk.Label(self.frame, text="Palindrome Checker",
                  style='TLabel').grid(row=0, column=0, columnspan=2)

        self.result_labels = []
        self.initiate_check_palindromes()

        # Additional criteria: Allow users to choose colors
        self.setup_color_options()

    def setup_color_options(self):
        color_frame = ttk.LabelFrame(
            self.frame, text="Color Options", padding=10)
        color_frame.grid(row=len(self.result_labels) + 1,
                         column=0, columnspan=2, sticky="w")

        ttk.Label(color_frame, text="Background Color:").grid(
            row=0, column=0, sticky="e")
        ttk.Label(color_frame, text="Button Color:").grid(
            row=1, column=0, sticky="e")
        ttk.Label(color_frame, text="Text Color:").grid(
            row=2, column=0, sticky="e")

        self.bg_color_var = tk.StringVar(value="white")
        self.btn_color_var = tk.StringVar(value="blue")
        self.text_color_var = tk.StringVar(value="black")

        ttk.Entry(color_frame, textvariable=self.bg_color_var).grid(
            row=0, column=1, padx=5)
        ttk.Entry(color_frame, textvariable=self.btn_color_var).grid(
            row=1, column=1, padx=5)
        ttk.Entry(color_frame, textvariable=self.text_color_var).grid(
            row=2, column=1, padx=5)

        ttk.Button(color_frame, text="Apply Colors",
                   command=self.apply_colors).grid(row=3, columnspan=2)

    def apply_colors(self):
        bg_color = self.bg_color_var.get()
        btn_color = self.btn_color_var.get()
        text_color = self.text_color_var.get()

        self.root.configure(background=bg_color)
        self.frame.configure(background=bg_color)
        self.style.configure(
            'TButton', background=btn_color, foreground=text_color)
        self.style.configure('TLabel', foreground=text_color)

    def read_strings(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def is_palindrome(self, string):
        def recursive_check(left, right):
            if left >= right:
                return True
            if string[left].lower() != string[right].lower():
                return False
            return recursive_check(left + 1, right - 1)

        return recursive_check(0, len(string) - 1)

    def process_list(self, strings):
        return [self.is_palindrome(string) for string in strings]

    def display_results(self, strings, palindromes):
        row = 1  # Start from row 1 to skip the title label

        for string, is_palindrome in zip(strings, palindromes):
            if is_palindrome:
                result = f"'{string}' is a palindrome"
            else:
                result = f"'{string}' is not a palindrome"

            text_color = self.text_color_var.get()  # Use user-selected text color
            label = ttk.Label(self.frame, text=result, foreground=text_color)
            label.grid(row=row, column=0, columnspan=2)
            self.result_labels.append(label)

            row += 1

    def initiate_check_palindromes(self):
        strings = self.read_strings('data_strings_01.txt')
        palindromes = self.process_list(strings)
        self.display_results(strings, palindromes)


def main():
    root = tk.Tk()
    app = PalindromeCheckerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
