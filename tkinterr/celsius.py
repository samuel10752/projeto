from tkinter import *
#back-end
def calculo():
    if in0_fr1.get().replace('.','',1).isdigit():
        lb1_fr2['text']=(float(in0_fr1.get())*1.8)+32      
        
          

#front-end
root = Tk()

root.geometry('500x100') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 

fr1 = Frame(root, background='black')
fr2 = Frame(root, background='black')

#Frame
fr1.pack()
fr2.pack()

#widgets
lb0_fr1 = Label(fr1,text='Insira Cº', font='Arial 25')
in0_fr1 = Entry(fr1, font='Arial 25')
bt0_fr2 = Button(fr2, text='Obtenha F', font='Arial 25', command=calculo)
lb1_fr2 = Label(fr2, text='Resultado', font='Arial 25')

lb0_fr1.grid(row=0, column=0, sticky=NSEW)
in0_fr1.grid(row=0, column=1, sticky=NSEW)
bt0_fr2.grid(row=1, column=0, sticky=NSEW)
lb1_fr2.grid(row=1, column=1, sticky=NSEW)

root.mainloop()