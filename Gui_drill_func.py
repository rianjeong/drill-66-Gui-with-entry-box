from tkinter import *
import tkinter as tk
from tkinter import filedialog
import time
import shutil
import os
import Gui_drill_main
import Gui_drill_Gui
from datetime import timedelta, datetime
import sqlite3

source_file = []
destination_file = []
sourceText = "Select Source"
destinationText = "Select Destination"
executeText = "Files Transfered"
nothing = "No Files Found"


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)

#defining functions for destination, source and execute

def destinationDir(self):
    destName = filedialog.askdirectory()
    self.Dest_button["text"] = str(destName) if destName else destinationText
    destination = destName + "/"
    destination_file.append(destination)
    print(destination)
    

def executeDir(self):
    findFile(self)
    self.Ex_button["text"] = str(executeText) if executeDir else executeText
    create_table()
    input_data()
    lastCopy()
    self.backup_entry.set(lastCopy())

def findFile(self):
    source = source_file[0]
    destination = destination_file[0]
    now = time.time()
    diff_sec = float(24*3600)
    before = now - diff_sec


    for files in os.listdir(source):
        src_file = os.path.join(source, files)
        dst_file = os.path.join(destination, files)
        st = os.stat(src_file)

        mod_time = datetime.fromtimestamp(st.st_mtime)
        new_time = time.mktime(mod_time.timetuple())
        if new_time > before:
            shutil.copy(src_file, dst_file)
            print("files have been transfered")
        else:
            print("Not a new file")

def sourceDir(self):
    sourceName = filedialog.askdirectory()
    self.Src_button["text"] = str(sourceName) if sourceName else sourceText
    source = sourceName + "/"
    source_file.append(source)
    print(source)

def create_table():
    conn = sqlite3.connect('timestamp.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS last_checked(file_ID INTEGER PRIMARY KEY, unix FLOAT, dateModified TEXT)")
    conn.commit()
    conn.close()

def input_data(): 
    conn = sqlite3.connect('timestamp.db')
    c= conn.cursor()
    unix = time.time()
    dateModified = time.ctime()
    c.execute("INSERT INTO last_checked(unix, dateModified) VALUES (?,?)", (unix, dateModified))
    conn.commit()

def lastCopy():
    new_date = ()
    conn = sqlite3.connect('timestamp.db')
    c = conn.cursor()

    try: new_date = c.execute(
        "SELECT dateModified FROM last_checked WHERE file_ID = (SELECT MAX(file_ID) FROM last_checked)").fetchone()
    except:
        new_date == None
        conn.close()
        return ("No date of last check")

    conn.close()
    again = new_date
    return again
    
    
    

if __name__ == "__main__":
    pass





