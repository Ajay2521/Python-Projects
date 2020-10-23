# This is an python GUI program which is used to conver the current vlue for different conutries.

# importing the modules
from tkinter import *

# creating a class called CurrencyConverter
class CurrencyConverter():

    # definfing a init function for the class TipCal
    def __init__(self):
        
        # creating a display window variable
        window = Tk()

        # setting up the title for the display window
        window.title("Currency Converter")

        # setting up the background for the display window
        window.configure(background="blue")

        # setting the width and height of the display window
        window.geometry("450x320")

        # making the display window as fixed size one
        window.resizable(width=False, height=False)

        # Creating labels to display text
        Label(window, font="Helvetica 12 bold", bg ="blue", text="Amout to Convert").grid(column = 1, row=3,padx=25, pady=20)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="Conversion Rate").grid(column = 1, row=5, padx=25, pady=20)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="Converted Amount").grid(column = 1, row=7, padx=25, pady=20)

        # creating entry box for variables.
        self.amount = StringVar()
        Entry(window, textvariable = self.amount, justify = RIGHT).grid(column = 2, row = 3, padx=50, pady=20)

        self.ConRate = StringVar()
        Entry(window, textvariable = self.ConRate, justify = RIGHT).grid(column = 2, row = 5, padx=50, pady=20)
        
        self.ConAmount = StringVar()
        Entry(window, textvariable = self.ConAmount, justify = RIGHT).grid(column = 2, row = 7, padx=50, pady=20)

        
        # Creating a button for converting feet to meter.
        convert_btn=Button(window, text="Convert", bg="purple", fg="white", width=15, command=self.convert,font="Helvetica 10 bold")
        convert_btn.grid(column=1, row=9,padx=15, pady=30)

        # Creating a button for clearing all the values.
        clear_btn=Button(window, text="Clear", bg="black", fg="white", width=15, command=self.clear,font="Helvetica 10 bold")
        clear_btn.grid(column=2, row=9,padx=15, pady=30)

        window.mainloop()

    # function to convert values
    def convert(self):
        conRate = float(self.ConRate.get())
        conAmount = float(self.amount.get()) * conRate
        self.ConAmount.set(format(conAmount, '10.2f'))
        

    # function to clear values
    def clear(self):
        self.amount.set("0")    # making a empty value in amount entry box
        self.ConRate.set("0")   # making a empty value in conversion rate entry box
        self.ConAmount.set("0") # making a empty value in converted amount entry box
        
CurrencyConverter()

