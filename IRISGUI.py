"""
Created on Wed Aug 04 2023

@author: Victor CHeng

IRIS GUI
"""

# import DrixitTest
# import IRISInter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

'''
===== Global Variables =====
'''
path = "C:\\Users\\slowl\\Desktop\\gitem\\Iris-GUI\\"
pathM = "C:\\Users\\mpmun\\CodeUsersMpmun\\Iris-GUI\\zappy.png"
GUIname = "IRIS Interactive Interface"
GUIsize = "500x500"
Zappy = path + "zappy.png"
Sammy = path + "sammy.png"

winMinSize = 500
iconSize = 75
titleFontSize = 20
rowGridSize = 6
columnGridSize = 4

'''
===== FUNCTIONS =====
'''



'''
===== GUI elements =====
'''
# images
zappyPic = Image.open(Zappy)
zappyIcon = ImageTk.PhotoImage(zappyPic)
resizedZappyIcon = zappyPic.resize((iconSize,iconSize), Image.ANTIALIAS)
resizedZappy = ImageTk.PhotoImage(resizedZappyIcon)

sammyPic = Image.open(Sammy)
sammyIcon = ImageTk.PhotoImage(sammyPic)
resizedSammyIcon = sammyPic.resize((iconSize,iconSize), Image.ANTIALIAS)
resizedSammy = ImageTk.PhotoImage(resizedSammyIcon)

# whatever bar photo
root.wm_iconphoto(True, zappyIcon)

# title bar
root.title(GUIname)
root.geometry(GUIsize)

# minimum GUI size
root.minsize(winMinSize, winMinSize)

# Icons, name, etc.
logo = Label(root, image = resizedZappy, height = iconSize, width = iconSize).grid(row = 0, column = 0)
ucsc = Label(root, image = resizedSammy, height = iconSize, width = iconSize).grid(row = 0, column = 3)
exeName = Label(root, text = GUIname, font = ["Comic sans MS", 14], justify = 'center').grid(row = 0, column = 1, columnspan = 2)

# mount USB button


# select/deselect all buttons


'''
===== Runs GUI =====
'''

# updates grid sizing
for i in range(rowGridSize):
    root.rowconfigure(i, weight=1, minsize=100)
    for j in range(columnGridSize):
        root.columnconfigure(j, weight=1, minsize=100)
    


# GUI loop
root.mainloop()
