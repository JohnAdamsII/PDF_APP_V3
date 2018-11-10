import sys
import os
import tkinter

master=tkinter.Tk()


master.title("PDF APP")
master.configure(background = 'gray20')

def RunConvertScript():
    os.system('python PDF_Converter.py')

def RunDeleteScript():
    os.system('python Delete_PDF.py')

def RunDocxScript():
    os.system('python docx_convert.py')
    os.system('python PDF_Merge_Script.py')

def RunMergeScript():
    os.system('python PDF_Merge_Script.py')

master.geometry("300x200")

A=tkinter.Button(master,text="Convert & Merge Image Files",command= RunConvertScript,background = 'sea green')
#A.grid(row=3,column=6, columnspan=2)
#A.pack()
A.place(x=80,y=50)

B=tkinter.Button(master,text="Delete PDF Files",command= RunDeleteScript,background = 'red')
B.place(x=80,y=130)

C = tkinter.Button(master,text="Convert & Merge docx Files",command= RunDocxScript,background = 'yellow')
C.place(x=80,y=90)
#B.grid(row=5,column=5, columnspan=2)
#B.pack()





master.mainloop()
