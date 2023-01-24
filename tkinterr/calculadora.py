from tkinter import *

#funçoes
def entrada(valor):
    lb['text'] += valor

def resultado():
    x=eval(lb['text'])
    lb['text']=str(x)

def limpar():
    lb['text'] =''


#janela
root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.geometry('862x400')


#widgets numéricos
lb = Label(root, text='', font='Arial 45', fg='green', bg='black')
bt1 = Button(root, text="0", font='Arial 28', command=lambda:entrada('0'))
bt2 = Button(root, text="9", font='Arial 28', command=lambda:entrada('9'))
bt3 = Button(root, text="8", font='Arial 28', command=lambda:entrada('8'))
bt4 = Button(root, text="7", font='Arial 28', command=lambda:entrada('7'))
bt5 = Button(root, text="6", font='Arial 28', command=lambda:entrada('6'))
bt6 = Button(root, text="5", font='Arial 28', command=lambda:entrada('5'))
bt7 = Button(root, text="4", font='Arial 28', command=lambda:entrada('4'))
bt8 = Button(root, text="3", font='Arial 28', command=lambda:entrada('3'))
bt9 = Button(root, text="2", font='Arial 28', command=lambda:entrada('2'))
bt10 = Button(root, text="1", font='Arial 28', command=lambda:entrada('1'))

#widgets simbolos
bt11 = Button(root, text="+", font='Arial 28', command=lambda:entrada('+'))
bt12 = Button(root, text="-", font='Arial 28', command=lambda:entrada('-'))
bt13 = Button(root, text="x", font='Arial 28', command=lambda:entrada('*'))
bt14 = Button(root, text="/", font='Arial 28', command=lambda:entrada('/'))
bt15 = Button(root, text=".", font='Arial 28', command=lambda:entrada('.'))
bt16 = Button(root, text='=', font='Arial 25', command=lambda:resultado())
bt17 = Button(root, text="C", font='Arial 28', command=lambda:limpar())
bt18 = Button (root, text='%', font= 'Arial 25', command=lambda: entrada('%'))
bt19 = Button (root, text='⌫', font= 'Arial 25', command=lambda: limpar())
bt20 = Button (root, text='√', font= 'Arial 25', command=lambda: entrada('√'))

#widgets #linha 0
root.geometry('300x440')
lb.grid(row=0, column=0, columnspan=4, sticky=NSEW )
bt17.grid(row=4, column=0,sticky=NSEW ) #C
bt14.grid(row=5, column=3,sticky=NSEW ) #/
bt15.grid(row=5,column=0,sticky=NSEW )#.
bt16.grid(row=4,column=2, sticky=NSEW) #= #linha 4
bt13.grid(row=2, column=3, sticky=NSEW) #X #linha 1
bt11.grid(row=4, column=3, sticky=NSEW) #+ #linha 3
bt12.grid(row=3, column=3, sticky=NSEW) #- #linha 2
bt18.grid(row=5, column=2, sticky=NSEW) #⌫ linha 5
bt19.grid(row=1, column=3, sticky=NSEW) #% linha 1
bt20.grid(row=5, column=1, sticky=NSEW) #√ linha 5

#Linha 1
bt4.grid(row=1, column=0, sticky=NSEW) #7
bt3.grid(row=1, column=1, sticky=NSEW) #8
bt2.grid(row=1, column=2, sticky=NSEW) #9

# linha 2
bt7.grid(row=2, column=0, sticky=NSEW) #4
bt6.grid(row=2, column=1, sticky=NSEW) #5
bt5.grid(row=2, column=2, sticky=NSEW) #6

#linha 3
bt10.grid(row=3, column=0, sticky=NSEW) #1
bt9.grid(row=3, column=1, sticky=NSEW) #2
bt8.grid(row=3, column=2, sticky=NSEW) #3

#linha 4
bt1.grid(row=4, column=1,sticky=NSEW) #0

#Rodar
root.mainloop()
