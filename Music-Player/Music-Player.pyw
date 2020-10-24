# This is an python GUI program which is used to play, stop, pause and unpause a music.

# importing the modules
import pygame
import os
from tkinter import *
from tkinter.filedialog import askdirectory as ad

# creating a display window variable
window = Tk()

# setting up the title for the display window
window.title("Music-Player")

# setting up the background for the display window
window.configure(background="blue")

# setting the width and height of the display window
window.geometry("500x430")

# making the display window as fixed size one
window.resizable(width=False, height=False)

# geeting folder where songs stored
Folder = ad()
os.chdir(Folder)

# song list and current song playing list
SongList = os.listdir()
PlayList = Listbox(window, font="Helvatica 8 bold", bg="yellow", selectmode = SINGLE,height=5, width = 30)

for song in SongList:
    pos = 0
    PlayList.insert(pos, song)
    pos = pos+1

pygame.init()
pygame.mixer.init()

# function to play the music
def play():
    pygame.mixer.music.load(PlayList.get(ACTIVE))
    var.set(PlayList.get(ACTIVE))
    pygame.mixer.music.play()

# function to stop the music
def stop():
    pygame.mixer.music.stop()

# function to pause the music
def pause():
    pygame.mixer.music.pause()

# function to unpause the music
def unpause():
    pygame.mixer.music.unpause()

var = StringVar()
SongTitle = Label(window, font ="Helvatica 9 bold", textvariable=var)
SongTitle.grid(padx=150, pady=30)

# button to play, stop, pause and unpause
play_btn = Button(window, width = 15, font ="Helvatica 11 bold", text = "PLAY",command = play, bg="green", fg = "white")
play_btn.grid(padx=150, pady=10)


stop_btn = Button(window, width = 15, font ="Helvatica 11 bold", text = "STOP" ,command = stop, bg="red", fg = "white" )
stop_btn.grid(padx=150, pady=10)

pause_btn = Button(window, width = 15, font ="Helvatica 11 bold", text = "PAUSE",command = pause, bg="purple", fg = "white" )
pause_btn.grid(padx=150, pady=10)

unpause_btn = Button(window, width = 15, font ="Helvatica 11 bold", text = "UNPAUSE",command = unpause, bg="black", fg = "white" )
unpause_btn.grid(padx=150, pady=10)

PlayList.grid(padx=150, pady=10)

window.mainloop()
        