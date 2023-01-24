# Importar biblioteca 
from cgitb import text
from distutils.command.build_py import build_py_2to3
from tkinter import *

# Criar janela  
root = Tk()
root.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #baclground color
root.minsize(width=100, height=100)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Criar os widgets
bt1 = Button(root, text="Botão 1")
bt2 = Button(root, text="Botão 2")
bt3 = Button(root, text="Botão 3")
bt4 = Button(root, text="Hallow")

# Organizar os Widgets 
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=2)
bt3.grid(row=0, column=1)
bt4.grid(row=1, column=0,columnspan=3, sticky=NSEW)

# Executar e manter tabela
root.mainloop()