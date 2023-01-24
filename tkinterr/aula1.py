from tkinter import *

#backend
def imprimir():
    lb1['text'] = in1.get()
    print(in1.get())

#window
janela = Tk()
janela.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
janela.config(background='#fff') #baclground color
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)

#widgets
lb1 = Label(janela, text="Wello World")
in1 = Entry(janela, font="Arial 15")
bt1 = Button(janela, text="sair", font="Arial 10", command=quit)
bt2 = Button(janela, text="Imprimir", font="Arial 10", command=imprimir)

#Layout
lb1.pack()
in1.pack()
bt1.pack()
bt2.pack()

#rum
janela.mainloop()


