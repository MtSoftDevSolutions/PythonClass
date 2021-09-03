from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os,time
import datetime as dt

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
        self.btnOrigin=Button(self.master, text="Source Folder", width=20, height=2, command=self.selectOrigin)
        self.btnOrigin.grid(row=1, column=0, columnspan=3,padx=(30,0),pady=(30,0)),
        self.btnDest=Button(self.master, text="Destination Folder", width=20, height=2, command=self.selectDest)
        self.btnDest.grid(row=1, column=6, columnspan=10,padx=(30,0),pady=(30,0)),
        self.btnSubmit=Button(self.master, text="Submit", width=10, height=2, command=self.transFiles)
        self.btnSubmit.grid(row=4, column=3, columnspan=3,padx=(30,0),pady=(30,0))
        
        # for example, an Entry widget, a Button widget, etc.

            # functions for the GUI go here
            # For Example:

    def selectOrigin(self):
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        self.entrySource.delete(0,"end")
        self.entrySource.insert(0, folder_selected)

    def selectDest(self):
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        self.entryDestination.delete(0,"end")
        self.entryDestination.insert(0, folder_selected)

    def transFiles(self):
        source = self.entrySource.get() #From selectOrigin we stored the folder path to self.entrySource.insert we get it back so that we can use it by using .get()
        print (source)
        destination = self.entryDestination.get()
        print(destination) #work to 
        now = dt.datetime.now()
        ago = now-dt.timedelta(hours=24)
        print(ago)
        strftime = "%H:%M %m/%d/%Y"
        for root, dirs, files in os.walk(source):
            for fName in files:
                path = os.path.join(root, fname) #fname is a variable, it is one that I created, could have been anything, just has to match the variable after for in line above
                st = os.stat(path) #st has many of the attributes about the files
                print(st)
                mtime = dt.datetime.fromtimestamp(st.st_mtime) #mtime is when we last used the file vs ctime would be when we created the file
                print(mtime)
                if mtime > ago:
                    print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                    shutil.move(path, dest)


            

    
if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
