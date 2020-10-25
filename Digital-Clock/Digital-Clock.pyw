# This is an python GUI program which is used to display the time.

# importing the modules
from tkinter import *
from time import strftime

# creating a display window variable
window = Tk()

# setting up the title for the display window
window.title("Digital Clock")

# setting up the background for the display window
window.configure(background="black")

# setting the width and height of the display window
window.geometry("300x250")

# making the display window as fixed size one
window.resizable(width=False, height=False)

# function used to display time

def time():
    timeFormat = strftime("%H:%M:%S %p")
    lbl.config(text = timeFormat)
    lbl.after(1000, time)

# creating and styling the label

lbl = Label(window, font = ("arial", 30, "bold"),bg ="black", fg="white")
lbl.pack(anchor = "center", fill = "both", expand=1)

# calling the function time

time()

window.mainloop()



