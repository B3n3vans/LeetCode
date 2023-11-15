import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

def call():
    res = mb.askquestion('User','Do you want Free Candies?')
    if res == 'yes':
        mb.showinfo('Gift','Here 🍬🍬')
        root.destroy()
    
    else:
        mb.showinfo('ok', 'ok')
        root.destroy()

root = tk.Tk()
canvas = tk.Canvas(root,
                   width=200,
                   height=200)

canvas.pack()
b = Button(root, text='Click Here!',
           command=call)

canvas.create_window(100,100,window=b)

root.mainloop()