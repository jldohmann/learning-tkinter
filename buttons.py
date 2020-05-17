from tkinter import *

root = Tk()
root.geometry('150x150')

def onEnter(e):
    myButton['background'] = 'green'

def onLeave(e):
    myButton['background'] = 'SystemButtonFace'

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

myButton.bind("<Enter>", onEnter)
myButton.bind("<Leave>", onLeave)

root.mainloop()
