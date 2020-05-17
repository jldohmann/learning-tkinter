from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('500x550')
root.title('Learn To Code at Codemy.com')

# Define the image
my_img = ImageTk.PhotoImage(Image.open("icon-python.png"))

# Put the image in something
my_label = Label(image=my_img)

# Put the thing on the screen
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()