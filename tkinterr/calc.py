from tkinter import *

janela = Tk()
janela.geometry('400x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
janela.config(background='#fff') #baclground color
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)

# def soma():
#     x = int(num1.get())
#     y= int(num2.get())

#     print(x + y)
#     z = (x + y)
#     result['text'] = z    

def soma():
    if num1.get().isnumeric() == 'False' or num2.get().isnumeric == 'False':
        print('')
    else:
        z = int(num1.get()) + int(num2.get())
        result['text'] = z

# widgets

labes1 = Label(janela, text="Digite o primeiro número")
num1 = Entry(janela, font='Georgia')

labes1.pack()
num1.pack()

labes2 = Label(janela, text="Digite o segundo número")
num2 = Entry(janela, font='Georgia')

labes2.pack()
num2.pack()

button = Button(janela, text="Somar", font="Georgia 10", command= soma)

button.pack()

result = Label(janela, text="O resultado é:", font='Georgia 10')

result.pack()

janela.mainloop()