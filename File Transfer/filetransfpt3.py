from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os

# class for the overall GUI
class ParentWindow(Frame):
    def __init__(self, master):
        # setting the frame configuration
        self.master = master
        #below sets the window to 700x400 without the possibility to resize
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        # gives the GUI frame a title
        self.master.title("File Transfer Select")
        #sets the background to gold
        self.master.config(bg='#FFD700')

        # Widgets for the GUI go here
        self.entrySource = Entry(self.master, text='Select Source Folder', font=("Engravers MT", 16), fg = 'green',bg='black')
        self.entrySource.grid(row=0, column=0, columnspan=3,padx=(30,0),pady=(30,0)),
        self.entryDestination = Entry(self.master, text='Select Destination Folder', font=("Engravers MT", 16), fg = 'green',bg='black')
        self.entryDestination.grid(row=0, column=6, columnspan=3,padx=(30,0),pady=(30,0)),
        #Syntax error shows up on line 26 and highlights B on Button. I was working with the file that I had when I was first learning Tkinter and following along with the video... Not sure what I'm doing wrong. 
        self.btnSrc=Button(self.master, text="Click to Select Source Folder", width=10, height=2), command=func1
        self.btnSrc.grid(row=2, column=0, columnspan=3,padx=(30,0),pady=(30,0)),
        self.btnDest=Button(self.master, text="Click to Select Destination Folder", width=10, height=2), command=func2
        self.btnDest.grid(row=2, column=6, columnspan=3,padx=(30,0),pady=(30,0)),
        self.btnSubmit=Button(self.master, text="Submit", width=10, height=2), command=func3
        
        # for example, an Entry widget, a Button widget, etc.

            # functions for the GUI go here
            # For Example:
def func1(self):
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    var1=folder_selected
def func2(self):
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    var2 = folder_selected
def func3(self):
    source = var1
    destination = var2
    files = os.listdir(source)
    for i in files:
        shutil.move(source+i,destination)
                

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
