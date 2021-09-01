from tkinter import *
import tkinter as tk

# We need to also import our other modules to have access to them
import webpage_generator_main
import webpage_generator_func

def load_gui(self):
    self.lbl_instruct = tk.Label(self.master, text='Insert Required Information and Click Corresponding Button')
    self.lbl_instruct.grid(row=0, column=0, columnspan=4, padx=(27,0), pady=(10,0), sticky=N+W)
   
    
    self.entry1 = tk.Entry(self.master)
    self.entry1.grid(row=1, column=0)



    self.btn_add = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: webpage_generator_func.horp(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    


    if __name__ == "__main__":
        pass
