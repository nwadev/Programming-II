from tkinter import *


class myApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Day Finder')
        self.root.geometry('640x480+300+300')
        self.root.resizable(False, False)
        self.root.option_add("*Font", "Times 14 normal")
        self.root.option_add('*Foreground', '#000000')
        self.root.configure(bg='#FFF8DC')
        self.root.option_add("*Label.Font", "Times 18 bold")

        # Month Data Entry
        Label(self.root, text="Month:").grid(row=0, column=0)
        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        self.month_var = StringVar(self.root)
        self.month_var.set(self.months[0])
        OptionMenu(self.root, self.month_var, *
                   self.months).grid(row=0, column=1)

        # Day Data Entry
        Label(self.root, text="Day:").grid(row=1, column=0)
        self.days = [str(i) for i in range(1, 32)]
        self.day_var = StringVar(self.root)
        self.day_var.set(self.days[0])
        OptionMenu(self.root, self.day_var, *self.days).grid(row=1, column=1)

        # Year Data Entry
        Label(self.root, text="Year:").grid(row=2, column=0)
        self.year_entry = Entry(self.root)
        self.year_entry.grid(row=2, column=1)

        # Calculate Button
        Button(self.root, text="Calculate",
               command=self.calculate).grid(row=3, column=0)

        # Result Label
        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=4, column=0)

        self.root.mainloop()

    def calculate(self):
        month = self.month_var.get()
        day = int(self.day_var.get())
        year = int(self.year_entry.get())

        leap_year = False
        if year % 400 == 0:
            leap_year = True
        elif year % 100 == 0:
            leap_year = False
        elif year % 4 == 0:
            leap_year = True

        month_num = self.months.index(month) + 1
        if month_num == 1 or month_num == 2:
            month_num += 12
            year -= 1

        k = year % 100
        j = year // 100

        day_of_week = (day + (13 * (month_num + 1)) //
                       5 + k + k // 4 + j // 4 + 5 * j) % 7

        days_of_week = ['Saturday', 'Sunday', 'Monday',
                        'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        result = days_of_week[day_of_week]
        self.result_label.config(text=result)


window1 = myApp()
