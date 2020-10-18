# This is an python GUI program which is used to bill amount by considering the tip percentage.

# importing the modules
from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry

# creating a class called TipCal
class TipCal():

    # definfing a init function for the class TipCal
    def __init__(self):
        
        # creating a display window variable
        window = Tk()

        # setting up the title for the display window
        window.title("Tip Calculator")

        # setting up the background for the display window
        window.configure(background="blue")

        # setting the width and height of the display window
        window.geometry("450x350")

        # making the display window as fixed size one
        window.resizable(width=False, height=False)

        # declaring the variables needed.
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost =  StringVar()

        # creating label for tip percentage.
        tip_percent = Label(window, text="Tip Percentage", bg="red", fg="black", width=15)
        tip_percent.grid(column=0, row=0, padx=15, pady=30)
        
        # creating label for meal amount.
        meal_amount = Label(window, text="Meal Amount", bg="green", fg="black", width=15)
        meal_amount.grid(column=1, row=1, padx=15)

        # creating a entry box for meal amount.
        meal_amount_entry = Entry(window, textvariable= self.meal_cost, width=15)
        meal_amount_entry.grid(column=2, row=1)

        # creating label for tip amount.
        tip_amount = Label(window, text="Tip Amount", bg="brown", fg="black", width=15)
        tip_amount.grid(column=1, row=3, padx=15)

        # creating a entry box for tip amount.
        tip_amount_entry = Entry(window, textvariable= self.tip, width=15)
        tip_amount_entry.grid(column=2, row=3)
        
        # creating label for total bill amount.
        total_bill = Label(window, text="Total bill", bg="red", fg="black", width=15)
        total_bill.grid(column=1, row=5, padx=15)

        # creating a entry box for tip amount.
        total_bill_entry = Entry(window, textvariable= self.total_cost, width=15)
        total_bill_entry.grid(column=2, row=5)
        
        # Creating a button for converting feet to meter.
        calculate_btn=Button(window, text="Calculate", bg="purple", fg="white", width=15, command=self.calculate)
        calculate_btn.grid(column=1, row=7,padx=15, pady=30)

        # Creating a button for clearing all the values.
        clear_btn=Button(window, text="Clear", bg="black", fg="white", width=15, command=self.clear)
        clear_btn.grid(column=2, row=7,padx=15, pady=30)

        # creating a radiobutton for tip percentage of different values
        five_precent= Radiobutton(window,text="05%",variable=self.tip_percent,value=5)
        five_precent.grid(column=0, row=1)
        ten_precent= Radiobutton(window,text="10%",variable=self.tip_percent,value=10)
        ten_precent.grid(column=0, row=2)
        fifteen_precent= Radiobutton(window,text="15%",variable=self.tip_percent,value=15)
        fifteen_precent.grid(column=0, row=3)
        twenty_precent= Radiobutton(window,text="20%",variable=self.tip_percent,value=20)
        twenty_precent.grid(column=0, row=4)
        twentyfive_precent= Radiobutton(window,text="25%",variable=self.tip_percent,value=25)
        twentyfive_precent.grid(column=0, row=5)
        

        window.mainloop()

    # function to calculate the tip amount and total bill amount    
    def calculate(self):

        pre_tip=float(self.meal_cost.get())
        percent= self.tip_percent.get() / 100
        
        tip_amount_entry = pre_tip * percent
        self.tip.set(tip_amount_entry)
        
        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    # function to clear values
    def clear(self):
        self.meal_cost.set("")  # making a empty value in meal amount entry box
        self.tip.set("")        # making a empty value in tip amount entry box
        self.total_cost.set("") # making a empty value in total bill entry box
        

TipCal()

        
