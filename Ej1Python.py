# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 06:39:45 2021

@author: Lenovo
"""

from tkinter import Tk, Label, Entry, Button, messagebox
def clickedSuma():
    a=int(txt1.get())
    b=int(txt2.get())
    c=a+b
    messagebox.showinfo("suma", c)

def clickedResta():
    a=int(txt1.get())
    b=int(txt2.get())
    c=a-b
    messagebox.showinfo("resta", c)

def clickedMultiplicacion():
    a=int(txt1.get())
    b=int(txt2.get())
    c=a*b
    messagebox.showinfo("multiplicacion", c)

def clickedDivision():
    a=int(txt1.get())
    b=int(txt2.get())
    c=a/b
    messagebox.showinfo("division", c)

window = Tk()
window.title("calculadora")
window.geometry("300x300")
lbl = Label(window, text="a")
lbl.grid(column=0, row=0)
lbl = Label(window, text="b")
lbl.grid(column=0,row=1)
txt1 = Entry(window, width=10)
txt1.grid(column=1,row=0)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)
btn = Button(window, text="Suma", command=clickedSuma)
btn.grid(column=0,row=2)
btn = Button(window, text="Resta", command=clickedResta)
btn.grid(column=1,row=2)
btn = Button(window, text="Multiplicacion", command=clickedMultiplicacion)
btn.grid(column=2,row=2)
btn = Button(window, text="Division", command=clickedDivision)
btn.grid(column=3,row=2)
window.mainloop()
