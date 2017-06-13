#!/usr/bin/python3
# Author Rian Jeong
# This is the the main exercise file to create my own GUI.  

from tkinter import *
from tkinter import ttk        
import tkinter as tk
import tkinter.messagebox


# other modules:
import Gui_drill_Gui
import Gui_drill_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        self.master = master
        self.master.resizable(width = True, height = False) 
        self.master.title("Python Drill GUI")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: Gui_drill_func.ask_quit(self))


       
        Gui_drill_Gui.load_gui(self)


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()          


