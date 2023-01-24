#import string
#from random import choice
#import time
#import string
#from itertools import combinations_with_replacement
#
#
#string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
#string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.digits # 0123456789
#string.punctuation # <=>?@[\]^_`{|}~.
#
#tamanho = 8
#valores = string.ascii_lowercase + string.digits
#senha = ''
#for i in range(tamanho):
#  senha += choice(valores)
#
#valores = string.ascii_letters + string.digits + string.punctuation
#
#def gerar_senhas(valores, tamanho):
#  comb = combinations_with_replacement(valores, tamanho)
#
#ini_t = time.time()
#gerar_senhas(valores, tamanho)
#fin_t = time.time()
#
#print("Tempo: " + str(fin_t - ini_t) + "s")
#print(senha)


import random
from tkinter import *
root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.janela()
        self.dados()
        root.mainloop()
    def janela(self):
        self.root.title("Gerador de senhas")
        self.root.configure(background= 'sky blue')
        self.root.geometry("400x400")
        self.root.resizable(True, True)
    def dados(self):
        ## Criação da label e entrada do site
        self.lb_site = Label(text="Site/Softwart", bg='#dfe3ee', fg='#107db2')
        self.lb_site.place(relx=0.15, rely=0.05)

        self.site_entry = Entry()
        self.site_entry.place(relx=0.35, rely=0.05, relwidth=0.5)
        ## Criação da label e entrada do site
        self.lb_site = Label(text="Site/Softwart", bg='#dfe3ee', fg='#107db2')
        self.lb_site.place(relx=0.15, rely=0.05)
        self.site_entry = Entry()
        self.site_entry.place(relx=0.35, rely=0.05, relwidth=0.5)
        ## Criação da label e entrada do usuário
        self.lb_email = Label(text="Email/Usuário", bg='#dfe3ee', fg='#107db2')
        self.lb_email.place(relx=0.15, rely=0.15)
        self.email_entry = Entry()
        self.email_entry.place(relx=0.36, rely=0.15, relwidth=0.5)
        ## Criação da label e entrada do Quantidade de caracteres
        self.quantcare = IntVar()
        self.lb_quantcare1 = Label(text="Quantidade de caracteres", bg='#dfe3ee', fg='#107db2')
        self.lb_quantcare1.place(relx=0.15, rely=0.25)
        self.quantcare1_entry = Entry(textvariable=self.quantcare)
        self.quantcare1_entry.place(relx=0.52, rely=0.25, relwidth=0.1)
        # Resultado
        self.resultadogeral = StringVar()
        self.lb_resultado1 = Label(text="Senha gerada ",
                            bg='#dfe3ee', fg='#107db2')
        self.lb_resultado1.place(relx=0.15, rely=0.35)
        self.resultado1 = Label(textvariable=self.resultadogeral)
        self.resultado1.place(relx=0.36, rely=0.35, relwidth=0.4)

        ### Criação do botao Gerar senha
        self.bt_geralsenha1 = Button(text="Gerar senha", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.gerarsenha)
        self.bt_geralsenha1.place(relx=0.3, rely=0.45, relwidth=0.3, relheight=0.1)
    def gerarsenha(self):
        num_caract = self.quantcare.get()
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        passwd = ""
        while len(passwd) != num_caract:
            passwd = passwd + random.choice(char_list)
        return self.resultadogeral.set(passwd)

Application()