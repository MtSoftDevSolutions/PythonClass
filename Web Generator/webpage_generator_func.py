
import os
from tkinter import *
import tkinter as tk
import sqlite3


# Be sure to import our other modules 
# so we can have access to them
import webpage_generator_main
import webpage_generator_gui
import webbrowser



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def horp(self):
    text = self.entry1.get()
    var1 = """<html><body><h3>"""+text+"""</h3></body></html>"""
    f=open("staytuned.html","w")
    f.write(var1)
    f.close()
    webbrowser.open("staytuned.html")

if __name__ == "__main__":
    pass
