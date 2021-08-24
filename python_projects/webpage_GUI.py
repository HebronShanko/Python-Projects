

# importing tkinter from python built in

from tkinter import *
import tkinter as tk
import webgenAssignement



class tkinter(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

# height and width of window tkinter
        self.master = master
        self.master.minsize(700,300) 
        self.master.maxsize(700,300)
        self.btn_add = tk.Button(self.master,width=50,height=10,text='Set a new body text of your choice',command=lambda: (webgenAssignement.userInput(self)))
        self.btn_add.grid(row=0,column=2,padx=(70,60),pady=(10,0),sticky=W)
        self.txt_body = tk.Entry(self.master,text='',textvariable=lambda: webgenAssignement.userInput(self))
        self.txt_body.grid(row=1,column=2,rowspan=1,columnspan=2,padx=(100,80),pady=(30,40),sticky=N+E+W) 


if __name__ == "__main__":
    root = tk.Tk()
    App = tkinter(root)
    root.mainloop()
