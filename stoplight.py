from tkinter import *
#need to install on all machines
from tkmacosx import Button


# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="yellow", background= "yellow")
green_button = Button(root, text="green",background= "green")
white_button = Button(root, text="color of light", background= "white")
#Add a label
label = Label(root, text="What color is the light")
textArea = Text(root, height=10, width=40,)

# Place widgets in window (with pack function!)
label.grid(row=1,column=1)
red_button.grid(row=0,column=0)
yellow_button.grid(row=0,column=1)
green_button.grid(row=0,column=2)
white_button.grid(row=3,column=0)
# Start the GUI event loop
textArea.grid( row=1, column=1, columnspan=2, rowspan=3)


root.mainloop()