from tkinter import *

from tkinter import messagebox

import random

def no():

    messagebox.showinfo('  ' ,"Thanks bro") 
    quit()

def motionMouse (event): 
    btnyes.place( x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk() 
root.geometry ('600x600')
root.title("survey")
root.resizable(width=False, height=False)
root['bg'] = 'white'

Label = Label(root, text='Are you gay?', font='Arial 20 bold', bg='white').pack()
btnyes = Button(root, text='No', font='Arial 28 bold') 
btnyes.place(x=170, y=100)
btnyes.bind('<Enter>', motionMouse) 
btnNo = Button(root, text='Yes', font='Arial 28 bold', command=no).place(x=350, y=100)

root.mainloop()