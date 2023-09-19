"""
Created on Wed Aug 04 2023

@author: Victor CHeng
testing: Mich P

IRIS GUI
"""

from IRISInter import *
from tkinter import *
from DrixitTest import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk as tt

# Important details for Tkinter to work (root)
root = Tk()
root.grid_rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

'''
===== Global Variables =====
'''
pathV = "C:\\Users\\slowl\\Desktop\\gitem\\Iris-GUI\\"
path = "C:\\Users\\mpmun\\CodeUsersMpmun\\Iris-GUI\\"
GUIname = "IRIS Interactive Interface"
GUIsize = "500x500"
Zappy = path + "zappy.png"
Sammy = path + "sammy.png"

winMinSizeX = 500
winMinSizeY = 650
iconSize = 75
titleFontSize = 20
rowGridSize = 15
columnGridSize = 4

'''
===== FUNCTIONS =====
'''

def refreshUSB():
    # new code here
    system = getOS("system")

    if system == "Windows":
        newM = MainWindows()
    else:
        newM = MainLinux()

    pathLabel = Label(mainFrame, text = newM.home, justify = 'center')
    pathLabel.grid(row = 2, column = 1, columnspan = 2)
    return newM

def promptPath(whichOne):
    # prompts user to select folder/directory or file
    if whichOne == "DIRECTORY":
        if getOS("system") == "Windows":
            osDir = "C:\\"
        elif getOS("system") == "Darwin" or getOS("system") == "Linux":
            osDir = "\\home"

        directoryName = fd.askdirectory()
        return directoryName
    
    elif whichOne == "FILE":
        allowedTypes = (('text files', '*.txt'),('All files', '*.*'))

        if getOS("system") == "Windows":
            osDir = "C:\\"
        elif getOS("system") == "Darwin" or getOS("system") == "Linux":
            osDir = "\\home"

        fileName = fd.askopenfilename(title = 'Select File', initialdir=osDir, filetypes = allowedTypes)
        return fileName
    
    else:
        return "INCORRECT PROMPT"
    
def manualSelectDir():
    directoryName = promptPath("DIRECTORY")
    pathLabel = Label(mainFrame, text = directoryName, justify = 'center')
    pathLabel.grid(row = 2, column = 1, columnspan = 2)
    return directoryName

def deselect():
    # new code here
    return

def select():
    # new code here
    return

def readFile():
    return

def writeFile():
    print("This button works")
    return

def copyFile():
    if syst() == "Windows":
        M = MainWindows()
        
    if syst() == "Linux":
        M = MainLinux()

    pathLabel = Label(mainFrame, text = M.home, justify = 'center')
    pathLabel.grid(row = 2, column = 1, columnspan = 2)
    return

def annihilateFile():
    warningBox = mb.askokcancel(title = "Are you sure about this, chief?", 
                                   message = "This action cannot be undone! \nDo you wish to proceed?", 
                                   icon = mb.WARNING)
    
    # This section deletes the files
    
    if warningBox:
        mb.showinfo(title = "Annihilated",
                    message = "Files deleted successfully")
        return
    return

def exitGui():
    exit()
    return

'''
===== GUI elements =====
'''
# images
zappyPic = Image.open(Zappy)
zappyIcon = ImageTk.PhotoImage(zappyPic)
resizedZappyIcon = zappyPic.resize((iconSize,iconSize), Image.LANCZOS)
resizedZappy = ImageTk.PhotoImage(resizedZappyIcon)

sammyPic = Image.open(Sammy)
sammyIcon = ImageTk.PhotoImage(sammyPic)
resizedSammyIcon = sammyPic.resize((iconSize,iconSize), Image.LANCZOS)
resizedSammy = ImageTk.PhotoImage(resizedSammyIcon)

# whatever bar photo
root.wm_iconphoto(True, zappyIcon)

# title bar
root.title(GUIname)
root.geometry(GUIsize)

# minimum GUI size
root.minsize(winMinSizeX, winMinSizeY)

# Main GUI frame
mainFrame = Frame(root)
mainFrame.grid(sticky='news')

for i in range(columnGridSize):
    mainFrame.columnconfigure(i, weight = 1)

for i in range(rowGridSize):
    mainFrame.grid_rowconfigure(i, weight = 1)

# Icons, name, etc. (row 0)
logo = Label(mainFrame, image = resizedZappy, height = iconSize, width = iconSize)
logo.grid(row = 0, column = 0)

ucsc = Label(mainFrame, image = resizedSammy, height = iconSize, width = iconSize)
ucsc.grid(row = 0, column = 3)

exeName = Label(mainFrame, text = GUIname, font = ["Comic sans MS", 14], justify = 'center')
exeName.grid(row = 0, column = 1, columnspan = 2)

# Tabular button [future addition] (row 1)

# Mount USB button (row 2)
refreshButton = Button(mainFrame, text = "Refresh USB", command = refreshUSB)
refreshButton.grid(row = 2, column = 0)

pathLabel = Label(mainFrame, text = "No path selected", justify = 'center')
pathLabel.grid(row = 2, column = 1, columnspan = 2)

choosePath = Button(mainFrame, text = "Manual Path", command = manualSelectDir)
choosePath.grid(row = 2, column = 3)

# File display window + deselect/select all buttons (row 3 - 6)
deselectAll = Button(mainFrame, text = "Deselect All", command = deselect)
deselectAll.grid(row = 3, column = 0)

selectAll = Button(mainFrame, text = "Select All", command = select)
selectAll.grid(row = 4, column = 0)




# Display window 1
canvasFrame1 = Frame(mainFrame, bg="yellow")
canvasFrame1.grid(row = 4, column = 1, rowspan = 4, columnspan = 3, pady=(5, 0))
canvasFrame1.grid_propagate(False)

windowCanvas1 = Canvas(canvasFrame1, bg="white")
windowCanvas1.grid(row=0, column=0, sticky="news")

vsb1 = Scrollbar(windowCanvas1, orient = "vertical", command = windowCanvas1.yview)
vsb1.grid(row = 0, column = 1, sticky='ns')
windowCanvas1.configure(yscrollcommand = vsb1.set)

listFrame = Frame(windowCanvas1)
windowCanvas1.create_window((0, 0), window = listFrame, anchor='nw')

listFrame.update_idletasks()

#canvasFrame1.config(scrollregion = canvasFrame1.bbox("all"))
# Spacer (row 7)

# Read, Write, Copy, Annihilate buttons (row 8)
readButton = Button(mainFrame, text = "Read File", command = readFile)
readButton.grid(row = 7, column = 0)

writeButton  = Button(mainFrame, text = "Insert File", command = writeFile)
writeButton.grid(row = 7, column = 1)

copyButton = Button(mainFrame, text = "Copy File", command = copyFile)
copyButton.grid(row = 7, column = 2)

annihilateButton  = Button(mainFrame, text = "Annihilate", command = annihilateFile)
annihilateButton.grid(row = 7, column = 3)

# Spacer (row 9)

# Read window (row 10 - 13)
newFrame = Frame(mainFrame, bg = "yellow")
newFrame.grid(row = 9, column = 1)

# Exit button (row 14)
exitButton = Button(mainFrame, text = "Exit GUI", command = exitGui)
exitButton.grid(row = 13, column = 1, columnspan = 2)

# Spacer (row 15)

'''
===== Runs GUI =====
'''
# GUI loop
root.mainloop()
