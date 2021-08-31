import webbrowser
import tkinter as tk
from tkinter import *
import function1





master = tk.Tk()
master.geometry('500x500')
master.title ("Add New Body Text")
tk.Label(master, text="Enter the new body text").grid(row=0)
background = tk.Entry(master)
background.place(x = 10, y = 10, width=400, height=300)
background.grid(rowspan=30, columnspan=30, sticky= N+S)
master['bg'] = '#ffbf00'


self.addButton = tk.Button(
    master,
    text = "Add New Text to Body",
    padx=10,
    pady=5,
    command= function1.webchange(self)
)
if __name__=='__main__':
        mainloop()
