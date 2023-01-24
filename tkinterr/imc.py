from tkinter import *

# Criar janela 
root = Tk()
root.geometry('500x300+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 

fr1 = Frame(root, background='black')
fr2 = Frame(root, background='black')


def calc():
    if kg_fr1.get().replace(".","",1).isdigit() and alt_fr1.get().replace(".", "", 1).isdigit():
        x = round(float(kg_fr1.get()) / (float(alt_fr1.get())**2),2)
        lb4_fr2['text'] = x   

        if x <18.5:
            lb5_fr2['text'] = "Abaixo do peso"
        elif x >18.5 and x < 24.9:
            lb5_fr2['text'] = "Peso ideal"
        elif x > 25 and x < 29.9:
            lb5_fr2['text'] = "Sobrepeso"
        elif x > 30 and x < 34.9:
            lb5_fr2['text'] = "Obesidade grau I"
        elif x > 35 and x < 39.9:
            lb5_fr2['text'] = "Obesidade grau II"
        else:
            lb5_fr2['text'] = "Obesidade grau III"
 

    else:
        lb4_fr2['text'] = "Tente novamente"



lb1_fr1 = Label(fr1, text="Calcule seu IMC", font="Georgia 15")

lb2_fr1 = Label(fr1, text="Digite seu peso")

kg_fr1 = Entry(fr1, font='Georgia', width=15)

lb3_fr1 = Label(fr1, text="Digite sua altura")

alt_fr1 = Entry(fr1, font='Georgia', width=15)

bt1_fr2 = Button(fr2, text="Calcular", command=calc, width=15)

lb4_fr2 = Label(fr2, text="Seu imc", font="Georgia 10", pady=10)

lb5_fr2 = Label(fr2, text="Teste agora", font="Georgia 10", pady=10)

#Frame
fr1.pack()
fr2.pack()

# Organizar os Widgets 
lb1_fr1.grid(row=0, column=0, sticky=NSEW)
lb2_fr1.grid(row=1, column=0, sticky=NSEW)
kg_fr1.grid(row=2, column=0)
lb3_fr1.grid(row=3, column=0, sticky=NSEW)
alt_fr1.grid(row=4, column=0)
bt1_fr2.grid(row=5, column=0)
lb4_fr2.grid(row=6, column=0, sticky=NSEW)
lb5_fr2.grid(row=7, column=0, sticky=NSEW)


# Executar e manter tabela
root.mainloop()