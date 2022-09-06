# Import the Required libraries
from tkinter import *


# Create an instance of tkinter frame or window
win= Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to display the message
def key_press(e):
   label.config(text="key pressed " + e.char)

# Create a label widget to add some text
label= Label(win, text= "", font= ('Helvetica 17 bold'))
label.pack(pady= 50)

# Bind the Mouse button event
win.bind('<KeyPress>',key_press)
win.mainloop()