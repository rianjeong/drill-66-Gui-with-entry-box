from tkinter import *
import tkinter as tk
import Gui_drill_main
import Gui_drill_func

def load_gui(self):

    img = tk.PhotoImage(file = "C:\\Users\\rianjeong\\Desktop\\Python 3 files\\copying.gif")

    self.img_label = tk.Label(self.master, image = img)
    self.img_label.grid(row = 0, column = 1)
    self.img_label.pack()
    
    self.backup_entry = StringVar()
    self.backup_entry.set(Gui_drill_func.lastCopy())
    
    self.Src_button = tk.Button(self.master, text = "Find Source", command = lambda: Gui_drill_func.sourceDir(self))
    self.Src_button.grid(row = 1, column = 1, sticky = N+E+S+W)

    self.Dest_button = tk.Button(self.master, text = "Find Destination", command = lambda: Gui_drill_func.destinationDir(self))
    self.Dest_button.grid(row = 2, column = 1, sticky =  N+E+S+W)

    self.Ex_button = tk.Button(self.master, text = "Execute", command = lambda: Gui_drill_func.executeDir(self))
    self.Ex_button.grid(row = 3, column = 1, sticky = N+S+E+W)

    self.Src_label = tk.Label(self.master, text = "Source File:",)
    self.Src_label.grid(row = 1, column = 0, sticky = W)

    self.Dest_label = tk.Label(self.master, text = "Destination File:")
    self.Dest_label.grid(row = 2, column = 0, sticky = W)

    self.Ex_label = tk.Label(self.master, text = "Execute File Move:")
    self.Ex_label.grid(row = 3, column = 0, sticky = W)

    self.label_dateChanged = tk.Label(self.master, text = "Date Last checked:")
    self.label_dateChanged.grid(row = 4, column = 0)

    self.entry_dateChanged = tk.Entry(self.master, width = 40, textvariable = self.backup_entry)
    self.entry_dateChanged.grid(row = 4, column = 1)

if __name__ == "__main__":
    pass
