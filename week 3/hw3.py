# Chukwueemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2
# date finder
from tkinter import *

# A list of days of the week
week_days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']


class MyApp:
    def __init__(self):
        # Create the app window
        self.root = Tk()
        self.root.title('Date Finder DarkMode')
        self.root.geometry('640x480+300+300')
        self.root.resizable(False, False)
        self.root.option_add("*Font", "Times 14 normal")
        self.root.option_add('*Foreground', '#ffffff')
        self.root.configure(bg='#000000')
        self.root.option_add("*Label.Font", "Times 18 bold")

        # Month Dropdown Choose your month
        Label(self.root, text="Month:", bg='#000000').grid(row=0, column=0)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.month_var = StringVar(self.root)
        self.month_var.set(months[0])
        OptionMenu(self.root, self.month_var, *months).grid(row=1, column=0)

        # Day Dropdown fo the day of the month
        Label(self.root, text="Day:", bg='#000000').grid(row=0, column=1)
        days = [str(i) for i in range(1, 32)]
        self.day_var = StringVar(self.root)
        self.day_var.set(days[0])
        OptionMenu(self.root, self.day_var, *days).grid(row=1, column=1)

        # Input your year
        Label(self.root, text="Year:", bg='#000000').grid(row=0, column=2)
        self.year_entry = Entry(self.root, bg='#000000', fg='#ffffff')
        self.year_entry.grid(row=1, column=2)

        # Output button
        Button(self.root, text="Output", command=self.solve).grid(
            row=2, column=0)

        # Results Label
        self.result_label = Label(self.root, text="", bg='#000000')
        self.result_label.grid(row=2, column=1, columnspan=2)

        #
        self.root.mainloop()

    def solve(self):
        # Get selected month, day, and year
        selected_month = self.month_var.get()
        selected_day = int(self.day_var.get())
        selected_year = int(self.year_entry.get())

        # calculate the actaul day of the week
        offset = (selected_year % 200) // 2
        day_of_week_index = (selected_day + 2 * offset + len(selected_month)
                             * (selected_year % 3) + selected_year // 100) % 7

        # Get the corresponding day of the week
        result_day = week_days[day_of_week_index]
        self.result_label.config(text=result_day)


# close up the app
date_app = MyApp()
