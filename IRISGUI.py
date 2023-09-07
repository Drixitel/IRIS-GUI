"""
Created on Wed Aug 04 2023

@author: Victor CHeng

IRIS GUI
"""

import DrixitTest
import IRISInter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

'''
===== Global Variables =====
'''
path = "C:\\Users\\slowl\\Desktop\\gitem\\Iris-GUI\\"
GUIname = "IRIS Interactive Interface"
GUIsize = "500x500"
Zappy = path + "zappy.png"

winMinSize = 500
iconSize = 75
titleFontSize = 20

'''
===== FUNCTIONS =====
'''



'''
===== GUI elements =====
'''
# images
pic = Image.open(Zappy)
icon = ImageTk.PhotoImage(pic)
resizedIcon = pic.resize((iconSize,iconSize), Image.ANTIALIAS)
resized = ImageTk.PhotoImage(resizedIcon)

# whatever bar photo
root.wm_iconphoto(True, icon)

# title bar
root.title(GUIname)
root.geometry(GUIsize)

# minimum GUI size
root.minsize(winMinSize, winMinSize)

# Icons, name, etc.
logo = Label(root, image = resized, height = iconSize, width = iconSize).grid(row = 0, column = 0)
exeName = Label(root, text = GUIname, font = ["Comic sans MS", 14], justify = 'center').grid(row = 0, column = 1)

# mount USB button


# select/deselect all buttons


'''
===== Runs GUI =====
'''

# updates grid sizing
for i in range(3):
    root.columnconfigure(i, weight=1, minsize=100)
    root.rowconfigure(i, weight=1, minsize=100)

# GUI loop
root.mainloop()
