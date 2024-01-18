# Chukwuemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2

import tkinter as tk
from tkinter import filedialog, messagebox


def readStrings(fileName):
   # Reads a list of strings from a file and returns the list and Handles FileNotFoundError using try-except.

    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()
            strings = [line.strip() for line in lines]
            return strings
    except FileNotFoundError:
        error_message = f"The file '{fileName}' could not be found."
        messagebox.showerror("File Not Found", error_message)
        return []


def isPalindrome(string):
    # Checks if a string is a palindrome using recursion.
    cleaned_string = string.lower().replace(" ", "")

    # Base case: If the string has 0 or 1 characters, it's a palindrome
    if len(cleaned_string) <= 1:
        return True

    # Compare the first and last characters
    if cleaned_string[0] != cleaned_string[-1]:
        return False

    # substring excluding the first and last characters
    return isPalindrome(cleaned_string[1:-1])


def processList(strings):
    # Checks if each string in a list is a palindrome.
    palindrome_status_list = []

    for string in strings:
        is_palindrome = isPalindrome(string)
        palindrome_status_list.append(is_palindrome)

    return palindrome_status_list


def displayResults(strings, palindromes):
    """Displays the palindrome check results in the GUI"""

    row = 2  # Starts at row 1

    for i in range(len(strings)):

        # Display the string
        string_label = tk.Label(
            text=strings[i], fg="#ffff00", bg="#000439", font=("Times New Roman", 14))
        string_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

        # Determine if palindrome or not
        if palindromes[i]:
            result = "Palindrome"
            color = "#00ff00"
        else:
            result = "Not a Palindrome"
            color = "#ff00ff"

        # Display the result
        result_label = tk.Label(text=result, fg=color, bg="#000439",
                                font=("Times New Roman", 14))
        result_label.grid(row=row, column=1, padx=10, pady=5, sticky="w")

        # Increment row for next string
        row += 1


def initiateCheckPalindromes():
    # Initiates the palindrome checking process:
    strings = readStrings("data_strings_01.txt")
    palindromes = processList(strings)
    displayResults(strings, palindromes)


def main():
    # customize the gui here
    root = tk.Tk()
    root.title("Chukwu's Palindrome Checker")

    """ Background: #0a0a0a (dark grey)
    Text: #00ff00 (bright green), #ff00ff (bright pink), #00ffff (bright cyan), #ffff00 (bright yellow) , purple (#301934)"""

    bg_color = "#000439"
    button_bg = "#00ffff"
    button_fg = "#301934"
    label_fg = "#ffff00"
    root.config(bg=bg_color)

    checkButton = tk.Button(text="Check Palindromes", command=initiateCheckPalindromes,
                            bg=button_bg, fg=button_fg)
    checkButton.grid(row=1, columnspan=2, pady=10)

    titleLabel = tk.Label(text="Palindrome Results",
                          font=("Times New Roman", 14), bg=bg_color, fg=label_fg)
    titleLabel.grid(row=0, columnspan=2)
    root.mainloop()


if __name__ == "__main__":
    main()
