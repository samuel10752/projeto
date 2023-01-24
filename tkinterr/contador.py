# Importar biblioteca 
from cgitb import text
from distutils.command.build_py import build_py_2to3
from tkinter import *
from turtle import onclick, width

from setuptools import Command

# Criar janela 
root = Tk()
root.geometry('600x10') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #baclground color
root.minsize(width=100, height=56)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.bind('+', lambda event: mais())
root.bind('-', lambda event: menos())

# Function

def mais():

    if lb1["text"] < 10:
        lb1["text"] += 1

        

def menos():
    if lb1["text"] > -10:
        lb1["text"] -= 1




# Criar os widgets
bt1 = Button(root, text="- 1", width=10,height=3, command=menos)
lb1 = Label(root, text=0, width=10)
bt3 = Button(root, text="+ 1", width=10, height=3, command=mais)

# Organizar os Widgets 
bt1.grid(row=0, column=0, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)
bt3.grid(row=0, column=2, sticky=NSEW)
# bt4.grid(row=1, column=0,columnspan=3, sticky=NSEW)

# Executar e manter tabela
root.mainloop()