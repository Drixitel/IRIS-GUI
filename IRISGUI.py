"""
Created on Wed Aug 04 2023

@author: Victor CHeng

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
path = "C:\\Users\\slowl\\Desktop\\gitem\\Iris-GUI\\"
pathM = "C:\\Users\\mpmun\\CodeUsersMpmun\\Iris-GUI\\zappy.png"
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

NO_PATH = "No path selected"

'''
===== FUNCTIONS =====
'''

def populateFiles(directory):
    fileListbox.delete(0, END)  # Clear previous entries

    for item in os.listdir(directory):
        fileListbox.insert(END, item)
    return

def refreshUSB():
    # new code here
    system = getOS("system")

    if system == "Windows":
        newM = MainWindows()
    else:
        newM = MainLinux()

    pathLabel.config(text = newM.home)

    readButton.config(state=NORMAL)
    copyButton.config(state=NORMAL)
    writeButton.config(state=NORMAL)
    annihilateButton.config(state=NORMAL)

    populateFiles(pathLabel.cget("text"))
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
    pathLabel.config(text = directoryName)

    readButton.config(state=NORMAL)
    copyButton.config(state=NORMAL)
    writeButton.config(state=NORMAL)
    annihilateButton.config(state=NORMAL)

    populateFiles(pathLabel.cget("text"))
    return

def deselect():
    fileListbox.selection_clear(0, END)
    return

def select():
    fileListbox.select_set(0, END)
    return

def readFile():
    path = pathLabel.cget("text") + "/"

    if len(fileListbox.curselection()) > 1:
        mb.showerror(title = "Cannot read multiple files", 
                     message = "GUI cannot display multiple files. Please select only one (1) file.", 
                     icon = mb.WARNING)
        return
    elif len(fileListbox.curselection()) == 0:
        mb.showerror(title = "Please select a file", 
                     message = "Please select only one (1) file.", 
                     icon = mb.WARNING)
        return

    filePath = path + fileListbox.get(fileListbox.curselection())

    with open(filePath, "r") as file:
        lines = file.readlines()
            
    fileReadbox.delete(0, END)

    for line in lines:
        fileReadbox.insert(END, line.strip())
    
    clearRead.config(state=NORMAL)
    return

def clearReadFile():
    fileReadbox.delete(0, END)
    clearRead.config(state=DISABLED)
    return

def getSetDir():
    print(pathLabel.cget("text"))
    return pathLabel.cget("text")

def writeFile():
    from shutil import copy
    USBDirectory = getSetDir()

    if USBDirectory == NO_PATH:
        mb.showwarning(title = "No Path", 
                                     message = "No USB path detected or selected.\nPlease insert USB or manually select path.", 
                                     icon = mb.WARNING)
        return

    fileDirectory = promptPath("FILE")

    copy(fileDirectory, USBDirectory)
    populateFiles(pathLabel.cget("text"))
    return
    
def copyFile():
    # THIS STEALS THE FILES!! BEWARE!!!!
    if syst() == "Windows":
        M = MainWindows()
    elif syst() == "Linux":
        M = MainLinux()

    pathLabel.config(text = M.home)
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

pathLabel = Label(mainFrame, text = NO_PATH, justify = 'center')
pathLabel.grid(row = 2, column = 1, columnspan = 2)

choosePath = Button(mainFrame, text = "Manual Path", command = manualSelectDir)
choosePath.grid(row = 2, column = 3)

# File display window + deselect/select all buttons (row 3 - 6)
deselectAll = Button(mainFrame, text = "Deselect All", command = deselect)
deselectAll.grid(row = 3, column = 0)

selectAll = Button(mainFrame, text = "Select All", command = select)
selectAll.grid(row = 4, column = 0)

# Display window 1
fileListbox = Listbox(mainFrame, width = 20, selectmode = EXTENDED)
fileListbox.grid(row = 3, column = 1, rowspan = 4, columnspan = 2, sticky='news')

scrollBar1 = Scrollbar(fileListbox, orient=VERTICAL)
scrollBar1.pack(side=RIGHT, fill=Y)

fileListbox.config(yscrollcommand = scrollBar1.set)
scrollBar1.config(command = fileListbox.yview)

# Spacer (row 7)

# Read, Write, Copy, Annihilate buttons (row 8)
readButton = Button(mainFrame, text = "Read File", command = readFile, state=DISABLED)
readButton.grid(row = 7, column = 0)

writeButton  = Button(mainFrame, text = "Insert File", command = writeFile, state=DISABLED)
writeButton.grid(row = 7, column = 1)

copyButton = Button(mainFrame, text = "Copy File", command = copyFile, state=DISABLED) # THIS STEALS THE FILES!! BEWARE!!!!
copyButton.grid(row = 7, column = 2)

annihilateButton  = Button(mainFrame, text = "Annihilate", command = annihilateFile, state=DISABLED)
annihilateButton.grid(row = 7, column = 3)

# Spacer (row 9)

# Read window (row 10 - 13)
fileReadbox = Listbox(mainFrame, width = 40)
fileReadbox.bindtags((fileReadbox, mainFrame, "all"))
fileReadbox.grid(row = 9, column = 1, rowspan = 4, columnspan = 2, sticky='news')

scrollBar2 = Scrollbar(fileReadbox, orient=VERTICAL)
scrollBar2.pack(side=RIGHT, fill=Y)

fileReadbox.config(yscrollcommand = scrollBar2.set)
scrollBar2.config(command = fileReadbox.yview)

# Clear text box button (row 13)
clearRead = Button(mainFrame, text="Clear Read Window", command=clearReadFile, state=DISABLED)
clearRead.grid(row = 12, column = 0)

# Exit button (row 14)
exitButton = Button(mainFrame, text = "Exit GUI", command = exitGui)
exitButton.grid(row = 13, column = 1, columnspan = 2)

# Spacer (row 15)

'''
===== Runs GUI =====
'''
# GUI loop
root.mainloop()
