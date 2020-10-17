# This is an python GUI program which is used to conver the feet into meter.

# importing the modules
from tkinter import *

# creating a display window variable
window = Tk()

# setting up the title for the display window
window.title("Feet to Meter Conveter")

# setting up the background for the display window
window.configure(background="blue")

# setting the width and height of the display window
window.geometry("350x300")

# making the display window as fixed size one
window.resizable(width=False, height=False)

# function to convert feet to meter
def convert():
    value = float(e1.get()) # converting the feetva;ue to float
    meter = value * 0.3048  # converting feet to meter
    v2.set("%.4f" % meter)  # displaying the result in meter entry box

# function to clear values
def clear():
    v1.set("") # making a empty value in feet entry box
    v2.set("") # making a empty value in meter entry box


# creating label for Feet
l1 = Label(window, text="Feet", bg="red", fg="black", width=15, font="bold")
l1.grid(column=0, row=0, padx=15, pady=30)

# creating entry box for Feet
v1=DoubleVar()
e1=Entry(window, textvariable=v1, width=15)
e1.grid(column=1, row=0)
e1.delete(0, 'end')

# creating label for meter
l2 = Label(window, text="Meter", bg="green", fg="black", width=15, font="bold")
l2.grid(column=0, row=1, padx=15, pady=30)

# creating entry box for Feet
v2=DoubleVar()
e2=Entry(window, textvariable=v2, width=15)
e2.grid(column=1, row=1)
e2.delete(0, 'end')

# Creating a button for converting feet to meter.
convert_btn=Button(window, text="Convert", bg="purple", fg="white", width=15, font="bold", command=convert)
convert_btn.grid(column=0, row=3,padx=15, pady=30)

# Creating a button for clearing all the values.
clear_btn=Button(window, text="Clear", bg="black", fg="white", width=15, font="bold", command=clear)
clear_btn.grid(column=1, row=3,padx=15, pady=30)

window.mainloop()