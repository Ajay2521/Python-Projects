# This is an python GUI program which is used to calculate the total loan amount to pay and monthly payable amount.

# importing the modules
from tkinter import *

# creating a class called CurrencyConverter
class LoanCalculator():

    # definfing a init function for the class TipCal
    def __init__(self):
        
        # creating a display window variable
        window = Tk()

        # setting up the title for the display window
        window.title("Loan Calculator")

        # setting up the background for the display window
        window.configure(background="blue")

        # setting the width and height of the display window
        window.geometry("450x430")

        # making the display window as fixed size one
        window.resizable(width=False, height=False)

        # Creating labels to display text
        Label(window, font="Helvetica 12 bold", bg ="blue", text="Interest Rate").grid(column = 1, row=3,padx=25, pady=20,sticky=W)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="No. of years").grid(column = 1, row=5, padx=25, pady=20,sticky=W)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="Loan Amount").grid(column = 1, row=7, padx=25, pady=20,sticky=W)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="Monthly Payment").grid(column = 1, row=9, padx=25, pady=20,sticky=W)

        Label(window, font="Helvetica 12 bold", bg ="blue", text="Total Payment").grid(column = 1, row=11, padx=25, pady=20,sticky=W)

        # creating entry box for variables.
        self.InterestRate = StringVar()
        Entry(window, textvariable = self.InterestRate, justify = RIGHT).grid(column = 2, row = 3, padx=50, pady=20)

        self.nYears = StringVar()
        Entry(window, textvariable = self.nYears, justify = RIGHT).grid(column = 2, row = 5, padx=50, pady=20)
        
        self.LoanAmount = StringVar()
        Entry(window, textvariable = self.LoanAmount, justify = RIGHT).grid(column = 2, row = 7, padx=50, pady=20)

        self.MonthlyPay = StringVar()
        Entry(window, textvariable = self.MonthlyPay, justify = RIGHT).grid(column = 2, row = 9, padx=50, pady=20)
        
        self.TotalPay = StringVar()
        Entry(window, textvariable = self.TotalPay, justify = RIGHT).grid(column = 2, row = 11, padx=50, pady=20)

        # Creating a button for converting feet to meter.
        calculate_btn=Button(window, text="Calculate", bg="purple", fg="white", width=15, command=self.calculate,font="Helvetica 10 bold")
        calculate_btn.grid(column=1, row=13,padx=15, pady=30)

        # Creating a button for clearing all the values.
        clear_btn=Button(window, text="Clear", bg="black", fg="white", width=15, command=self.clear,font="Helvetica 10 bold")
        clear_btn.grid(column=2, row=13,padx=15, pady=30)

        window.mainloop()

    # function to calculate loan
    def calculate(self):
        monthlyPay = self.getMonthlypay(
            float(self.LoanAmount.get()),
            float(self.InterestRate.get()) / 1200,
            int(self.nYears.get())
        )
        self.MonthlyPay.set(format(monthlyPay, '10.2f'))

        totalPay = float(self.MonthlyPay.get()) * 12 * int(self.nYears.get())
        self.TotalPay.set(format(totalPay, '10.2f'))

    # function to calculate loan
    def getMonthlypay(self, loanAmount, interestRate, nYear):
        monthlyPay = loanAmount * interestRate / (1-1/(1+ interestRate) ** (nYear * 12))
        return monthlyPay

    # function to clear values
    def clear(self):
        self.LoanAmount.set("0")    
        self.InterestRate.set("0")   
        self.nYears.set("0") 
        self.MonthlyPay.set("0")
        self.TotalPay.set("0")

LoanCalculator()