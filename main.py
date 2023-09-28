# move an Image on the canvas with tkinter
 
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
# Create the window with the Tk class
root = tk.Tk()
eplotis = root.winfo_screenwidth()
eaukstis = root.winfo_screenheight()
veikejoaukstis = round(eaukstis / 8)
veikejoplotis = round(eplotis / 11)
x = 1
y = 1
# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=eplotis, height=eaukstis)
canvas.pack() # this makes it visible

# Loads and create image (put the image in the folder)
image = Image.open("taip.png")
image = image.resize((veikejoplotis,veikejoaukstis), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(image)
image = canvas.create_image(1, 1, anchor=tk.NW, image=pic)
 
 
def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(image, -10, 0)
    elif event.char == "d":
        canvas.move(image, 10, 0)
    elif event.char == "w":
        canvas.move(image, 0, -10)
    elif event.char == "s":
        canvas.move(image, 0, 10)
 
# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)
 
# this creates the loop that makes the window stay 'active'
root.mainloop()