# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Umran Alhaja.

"""

from tkinter import *
import shutil 
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

def openWindow():
    read=easygui.fileopenbox()
    return read
#1-------------
def makeFolder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of the new Folder")
    
    newFolder=input()
    path=os.path.join(newFolderPath,newFolder)
    
    os.mkdir(path)
    mb.showinfo("Done!","Folder Created !")
#2-------------
def deleteFolder():

    delFolder=filedialog.askdirectory()
    os.rmdir(delFolder)
    
    mb.showinfo('Done!','Folder Deleted!')
#3-------------
def createFile():
    newFilePath=filedialog.askdirectory()
    print("Name your file!!")
    fileName=str(input())
    
    f=open(fileName,"a")
    f.close()
#4-------------
def writeFile():
    file=filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    f=open(file,"a")
    print("Write your text here !")
    text=input()
    
    f.writeline(str(text))
    f.close()
#5--------------
def openFile():
    string=openWindow()
    try:
        os.startfile(string)
    except:
        mb.showinfo("Attention!","File not found!")
#6--------------
def deleteFile():
    del_file = openWindow()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo("Attention!","File not found!")
#7--------------
def copyFile():
    source1=openWindow()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo("Done!","File copied!")
#8---------------
def renameFile():
    chosenFile = openWindow()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")
#9---------------  
def moveFile():
    source = openWindow()
    destination=filedialog.askdirectory()
    if (source==destination):
        mb.showinfo("Attention!!","source and destination are same!")
    else:
        shutil.move(source,destination)
        mb.showinfo("Confirmation!","File Moved!")

root=Tk()
#create canvas to insert image
#canv=Canvas(root,width=500,height=420,bg='white')
#canv.grid(row=0,column=2)

#img=ImageTK.PhotoImage(Image.open("C:\\Users\\Umran\\OneDrive\\Pictures\\palestine logo.png"))  
#canv.create_image(20, 20, anchor=NW, image=img)

#create label and buttons
Label(root, text="UM File Manager", font=("Helvetica", 12), fg="blue").grid(row = 5, column = 2)
root.title('File Manager')
Button(root,text="Make a Folder",command=makeFolder).grid(row=15,column=2)
Button(root,text="Delete a Folder",command=deleteFolder).grid(row=25,column=2)
Button(root,text="Create a File",command=createFile).grid(row=35,column=2)
Button(root,text="Write in File",command=writeFile).grid(row=45,column=2)


Button(root,text="Open a File",command=openFile).grid(row=55,column=2)
Button(root,text="Delete File",command=deleteFile).grid(row=65,column=2)
Button(root,text="Copy File",command=copyFile).grid(row=75,column=2)
Button(root,text="Move a File",command=moveFile).grid(row=85,column=2)
Button(root,text="Rename a File",command=renameFile).grid(row=95,column=2)
root.mainloop()