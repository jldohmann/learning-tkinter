from tkinter import *

root = Tk()
root.geometry('150x150')

# Event functions
def onEnter(e):
    myButton['background'] = 'green'

def onLeave(e):
    myButton['background'] = 'SystemButtonFace'

def onRelease(e):
    myButton['background'] = 'SystemButtonFace'

# Return function

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

# Button creation and binding
# Button has red background when clicked

myButton = Button(root, text="Click Me!", activebackground='red', command=myClick)

myButton.bind("<Enter>", onEnter)
myButton.bind("<Leave>", onLeave)
myButton.bind("<ButtonRelease-1>", onRelease)

myButton.pack()

root.mainloop()
