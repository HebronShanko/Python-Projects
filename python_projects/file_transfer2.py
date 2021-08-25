


# Importing necessary packages
import shutil
import glob
import os
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
     
 
# Defining CreateWidgets() function to
# create necessary tkinter widgets

def CreateWidgets():
    link_Label = Label(root, text ="Select The File To move :",
                    bg = 'white')
    link_Label.grid(row = 1, column = 0,
                    pady = 5, padx = 5)
     
    root.sourceText = Entry(root, width = 50,
                            textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1,
                        pady = 5, padx = 5,
                        columnspan = 2)
     
    source_browseButton = Button(root, text ="Browse",
                                command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3,
                            pady = 5, padx = 5)
     
    destinationLabel = Label(root, text ="Select The Destination : ",
                            bg ='white')
    destinationLabel.grid(row = 2, column = 0,
                        pady = 5, padx = 5)
     
    root.destinationText = Entry(root, width = 50,
                                textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1,
                            pady = 5, padx = 5,
                            columnspan = 2)
     
    dest_browseButton = Button(root, text ="Browse",
                            command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3,
                        pady = 5, padx = 5)
     
    copyButton = Button(root, text ="Move Files",
                        command = MoveFile, width = 15)
    copyButton.grid(row = 3, column = 1,
                    pady = 5, padx = 5)
     
    
 
def SourceBrowse():
     
    #guide to find where users files are
    
    browse = filedialog.askdirectory(initialdir ="/Users/Hebron/Desktop/New Folder B")
     
    # Displaying the selected files in the root.sourceText
    # Entry using root.sourceText.insert()
    root.sourceText.insert(0, browse)
     
def DestinationBrowse():
    # which files are to be copied using the
   
    destinationdirectory = filedialog.askdirectory(initialdir ="/Users/Hebron/Desktop/New Folder A")
    # show the directory
    
    root.destinationText.insert('0', destinationdirectory)
     
     
def MoveFile():
    # source directory
    browse = root.sourceText.get()
    files_list = os.listdir(browse)
    # last modified date


    #modified within 24 hours
    desDir = root.destinationText.get() 
    for f in files_list:
        full_path = os.path.join(browse, f)
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
        todaysDate = datetime.datetime.now()
        modifyDateLimit = todaysDate - datetime.timedelta(days=1)
        if modifyDateLimit <= modifyDate:
            shutil.move(full_path, desDir)
            messagebox.showinfo("Successful")
    
     
    # Retrieving the source file selected by the
    # user in the SourceBrowse() and storing it in a
   
    
 
    
# storing in destination_location
   
 
# Looping through the files present in the list
    
# Moving the file to the destination using
        
        
 
# Creating object of tk class
root = tk.Tk()
     
# Setting the title and background color
# disabling the resizing property
root.geometry("830x120")
root.title("File_Transfer")
root.config(background = "grey")
     
# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()
     
# Calling the CreateWidgets() function
CreateWidgets()
     
# Defining infinite loop
root.mainloop()
