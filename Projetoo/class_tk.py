#CONSTRUÇÃO EWERSON
from tkinter import messagebox
import mysql.connector
#Breno
from cgitb import text
from tkinter import messagebox
from tkinter import *
from class_cadastro import *
from class_cotacao import*
#Samuel
from email.mime import image
from logging import root
from math import fabs
from struct import pack
from time import time
from tkinter import *
#CONSTRUÇÃO EWERSON

import tkinter as tk
from turtle import title, width


#CONSTRUÇÃO EWERSON
cotar = Cotacao()
cadastrar = Cadastro()
#CONSTRUÇÃO EWERSON

root = Tk()
root.title("Portal Investidor")
root.resizable(height = False, width = False)
root.geometry("484x560+800+155")
root.iconbitmap(default="icones\\ico.ico")

fr0 = Frame()
fr1 = Frame()
fr2 = Frame()
#fr3 = Frame()
fr4 = Frame()
fr5 = Frame()

# Variáveis globais

#CONSTRUÇÃO EWERSON
def logando():
    mysqldb = mysql.connector.connect(host='localhost',user='root',password='q1w2e3',database='investimentos')
    mycursor = mysqldb.cursor()
    global user, xad
    user = fr0_in2.get()
    passw = fr0_in3.get()
    sql = 'select nome, senha from Usuarios where cpf_cnpj = %s and senha = %s'
    mycursor.execute(sql, [(user), (passw)])
    results = mycursor.fetchall()
    if results:
        x=results[0]
        messagebox.showinfo('', 'login')
        fr0.grid_remove()
        fr2.grid()
        fr2_lab17['text']=x[0]
        root.geometry("1289x600+310+153")
        return True
        
    else: 
        messagebox.showinfo('','erro')

def fazer_cadastro():
    cpf_cnpj = fr1_in0.get()
    nome = fr1_in2.get()
    dataNasc = fr1_in3.get()
    telefone = fr1_in4.get()
    senha = fr1_in1.get()
    cadastrar.cadastro(cpf_cnpj, nome, dataNasc, telefone, senha)
#CONSTRUÇÃO EWERSON

# Letras maiusculas telas 
var1 =StringVar()
def maiusculo(*args):
    var1.set(var1.get().upper())
var1.trace("w", maiusculo)

var2 =StringVar()
def maiusculo(*args):
    var2.set(var2.get().upper())
var2.trace("w", maiusculo)

var3 =StringVar()
def maiusculo(*args):
    var3.set(var3.get().upper())
var3.trace("w", maiusculo)

var4 =StringVar()
def maiusculo(*args):
    var4.set(var4.get().upper())
var4.trace("w", maiusculo)

#tela do nome
var5 =StringVar()
def maiusculo(*args):
    var5.set(var5.get().title())
var5.trace("w", maiusculo)

#limpar o Label do montante na tela comprar
#def clear_1():
#    fr3_lab7['text'] =''
#    fr3_in1.delete(0,'end')
#    fr3_in2.delete(0,'end')
#    fr3_in4.delete(0,'end')
#limpar o entre da moeda na tela vender
def clear_2():
    fr4_lab7['text'] =''
    fr4_in1.delete(0,'end')
    fr4_in2.delete(0,'end')
#    fr4_in3.delete(0,'end')  
#limpar o entre da moeda na tela guardar
def clear_3():
    fr5_lab7['text'] =''
    fr5_in1.delete(0,'end')
    fr5_in2.delete(0,'end')
    fr5_in3.delete(0,'end')   
#limpar a tela de login
def clear_4():
    fr0_in2.delete(0,'end')
    fr0_in3.delete(0,'end')

def nome(event=None):
    x=fr1_in2.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] not in '0123456789':
            y+=x[i]
    fr1_in2.delete(0, 'end')
    fr1_in2.insert(0, y)

def vender(event=None):
    x=fr4_in1.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] not in '0123456789':
            y+=x[i]
    fr4_in1.delete(0, 'end')
    fr4_in1.insert(0, y)

def inserir(event=None):
    x=fr5_in1.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] not in '0123456789':
            y+=x[i]
    fr5_in1.delete(0, 'end')
    fr5_in1.insert(0, y)


#Data de nascimento

def data_nasc(event=None):
    x=fr1_in3.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [3,5]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    fr1_in3.delete(0, 'end')
    fr1_in3.insert(0, y)

#telefone Cadastro
def telefone_cadastro(event=None):
    x=fr1_in4.get().replace('(','').replace(')', '').replace('-', '')[:12]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [0]:
            y+= '(' + x[i]
        elif i in [2]:
            y+= x[i] + ')'
        elif i in [3, 7]:
            y+= x[i] + '-'
        else:
            y+=x[i]
    fr1_in4.delete(0, 'end')
    fr1_in4.insert(0, y)

#tela do capital tempo
#def compra_tempo(event=None):
#    x=fr3_in4.get()
#    y=''
#    if event.keysym.lower() == "backspace": return
#    for i in range(len(x)):
#        if x[i] in '0123456789':
#            y+=x[i]
#    fr3_in4.delete(0, 'end')
#    fr3_in4.insert(0, y)

#venda moeda investi
#def venda_moedacompra(event=None):
#    x=fr3_in4.get()
#    y=''
#    if event.keysym.lower() == "backspace": return
#    for i in range(len(x)):
#        if x[i] in '0123456789':
#            y+=x[i]
#    fr3_in4.delete(0, 'end')
#    fr3_in4.insert(0, y)


#venda moeda comprar
#def venda_moedainvesti(event=None):
#    x=fr4_in3 .get()
#    y=''
#    if event.keysym.lower() == "backspace": return
#    for i in range(len(x)):
#        if x[i] in '0123456789':
#            y+=x[i]
#    fr4_in3 .delete(0, 'end')
#    fr4_in3 .insert(0, y)

#guadar tempo    
def guarda_tempo(event=None):
    x=fr5_in3 .get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y+=x[i]
    fr5_in3 .delete(0, 'end')
    fr5_in3 .insert(0, y)

# Compra capital tela 
#def comprar_capital(event=None):
#    x = fr3_in2 .get().replace(',', '.')
#    y = ''
#    if event.keysym.lower() == "backspace": return
#    for i in range(len(x)):
#        if x[i] in '0123456789':
#            y += x[i]
#        elif x[i] in '.':
#            y += x[i]
#        else:
#            y += ''
#    if y.count('.') > 1:
#        y=y[:-1]
#    fr3_in2 .delete(0, 'end')
#    fr3_in2 .insert(0, y)

# guarada capital tela 
def guarda_capital(event=None):
    x = fr5_in2 .get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    fr5_in2 .delete(0, 'end')
    fr5_in2 .insert(0, y)    

#Venda capital tela
def venda_capital(event=None):
    x = fr4_in2 .get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    fr4_in2 .delete(0, 'end')
    fr4_in2 .insert(0, y)

#guadar capital tela
def guarda_capital(event=None):
    x = fr5_in2 .get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    fr5_in2 .delete(0, 'end')
    fr5_in2 .insert(0, y)



def cpf(event=None):
    x=fr0_in2.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    fr0_in2.delete(0, 'end')
    fr0_in2.insert(0, y)

def cpf_1(event=None):
    x=fr1_in0.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    fr1_in0.delete(0, 'end')
    fr1_in0.insert(0, y)

def cnpj(event=None):
    x=fr0_in2.get().replace('.','').replace('/', '').replace('-', '')[:14]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '01234567891011':
            if i in [1,4]:
                y+=x[i] + '.'
            elif i == 7:
                y+=x[i] + '/'
            elif i == 11:
                y+=x[i] + '-' 
            else:
                y+=x[i]
    fr0_in2.delete(0, 'end')
    fr0_in2.insert(0, y)


def cnpj_1(event=None):
            x=fr1_in0.get().replace('.','').replace('/', '').replace('-', '')[:14]
            y=''
            if event.keysym.lower() == "backspace": return
            for i in range(len(x)):
                if x[i] in '01234567891011':
                    if i in [1,4]:
                        y+=x[i] + '.'
                    elif i == 7:
                        y+=x[i] + '/'
                    elif i == 11:
                        y+=x[i] + '-' 
                    else:
                        y+=x[i]
            fr1_in0.delete(0, 'end')
            fr1_in0.insert(0, y)

#Cálculos Button fr3_bt5
#def comprar_confirmar():
#    #fr3_in1.get() #MOEDA
#    #fr3_in2.get() #CAPITAL
#    #fr3_in4.get() #TEMPO
#    if fr3_in1.get() == 'DOLAR':
#        j=float(fr2_lab['text'])
#        c=float(fr3_in2.get())
#        t=float(fr3_in4.get())
#        m = c * ((1 + j/100)**t)


#Chamando cotação de todas as moedas
def chama_cotacao():
    cotar.dolar() 
    fr2_lab7['text']=cotar.d
    cotar.euro()
    fr2_lab8['text']=cotar.e
    cotar.libra()
    fr2_lab9['text']=cotar.l
    cotar.bitcoin()
    fr2_lab10['text']=cotar.b
    cotar.ethereum()
    fr2_lab11['text']=cotar.et

    #cotar.dolar() 
    #fr3_lab8['text']=cotar.d
    #cotar.euro()
    #fr3_lab9['text']=cotar.e
    ##cotar.libra()
    #fr3_lab10['text']=cotar.l
    ##cotar.bitcoin()
    #fr3_lab11['text']=cotar.b
    ##cotar.ethereum()
    #fr3_lab12['text']=cotar.et

    #cotar.dolar()
    fr4_lab8['text']=cotar.d
    #cotar.euro()
    fr4_lab9['text']=cotar.e
    #cotar.libra()
    fr4_lab10['text']=cotar.l
    #cotar.bitcoin()
    fr4_lab11['text']=cotar.b
    #cotar.ethereum()
    fr4_lab12['text']=cotar.et

    #cotar.dolar()
    fr5_lab8['text']=cotar.d
    #cotar.euro()
    fr5_lab9['text']=cotar.e
    #cotar.libra()
    fr5_lab10['text']=cotar.l
    #cotar.bitcoin()
    fr5_lab11['text']=cotar.b
    #cotar.ethereum()
    fr5_lab12['text']=cotar.et

#Chama todas as médias das moedas nos últimos 3 meses, dentro dos label's
def chama_media():
    cotar.dolar1()
    fr2_lab12['text']=cotar.d3
    cotar.euro1()
    fr2_lab13['text']=cotar.e3
    cotar.libra1()
    fr2_lab14['text']=cotar.l3
    cotar.bitcoin1()
    fr2_lab15['text']=cotar.b3
    cotar.ethereum1()
    fr2_lab16['text']=cotar.et3

    #cotar.dolar() 
    #fr3_lab13['text']=cotar.d3
    ##cotar.euro()
    #fr3_lab14['text']=cotar.e3
    ##cotar.libra()
    #fr3_lab15['text']=cotar.l3
    ##cotar.bitcoin()
    #fr3_lab16['text']=cotar.b3
    ##cotar.ethereum()
    #fr3_lab17['text']=cotar.et3

    #cotar.dolar()
    fr4_lab13['text']=cotar.d3
    #cotar.euro()
    fr4_lab14['text']=cotar.e3
    #cotar.libra()
    fr4_lab15['text']=cotar.l3
    #cotar.bitcoin()
    fr4_lab16['text']=cotar.b3
    #cotar.ethereum()
    fr4_lab17['text']=cotar.et3

    #cotar.dolar()
    fr5_lab13['text']=cotar.d3
    #cotar.euro()
    fr5_lab14['text']=cotar.e3
    #cotar.libra()
    fr5_lab15['text']=cotar.l3
    #cotar.bitcoin()
    fr5_lab16['text']=cotar.b3
    #cotar.ethereum()
    fr5_lab17['text']=cotar.et3

def escolha_guardar():
    cod = 0
    nome_atk = user     
    nome_moeda = str(fr5_in1.get())
    capital = float(fr5_in2.get())
    meses = int(fr5_in3.get())
    if nome_moeda == 'DOLAR' or nome_moeda == 'DÓLAR':
        print('1')
        cotar.dolar2(meses)
        montante = cotar.md + capital
        cadastrar.cadastro_movimentacao(cod, nome_atk, nome_moeda, capital, meses, montante)
        fr5_lab7['text']=montante
    if nome_moeda == 'EURO':
        print('2')
        cotar.euro2(meses)
        montante = cotar.me + capital
        cadastrar.cadastro_movimentacao(cod, nome_atk, nome_moeda, capital, meses, montante)
        fr5_lab7['text']=montante
    if nome_moeda == 'LIBRA':
        print('3')
        cotar.libra2(meses)
        montante = cotar.ml + capital
        cadastrar.cadastro_movimentacao(cod, nome_atk, nome_moeda, capital, meses, montante)
        fr5_lab7['text']=montante
    if nome_moeda == 'BITCOIN':
        print('4')
        cotar.bitcoin2(meses)
        montante = cotar.mb + capital
        cadastrar.cadastro_movimentacao(cod, nome_atk, nome_moeda, capital, meses, montante)
        fr5_lab7['text']=montante
    if nome_moeda == 'ETHEREUM':
        print('5')
        cotar.ethereum2(meses)
        montante = cotar.met + capital
        cadastrar.cadastro_movimentacao(cod, nome_atk, nome_moeda, capital, meses, montante)
        fr5_lab7['text']=montante

def escolha_vender():
    cod_n = 0
    nome_atk_n = user     
    nome_moeda_n = str(fr4_in1.get())
    capital_n = float(fr4_in2.get())
    if nome_moeda_n == 'DOLAR' or nome_moeda_n == 'DÓLAR':
        print('1')
        cotar.dolar()
        montante_n = float(cotar.d) + float(capital_n)
        cadastrar.cadastro_movimentacao(cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n)
        fr5_lab7['text']=montante_n
    if nome_moeda_n == 'EURO':
        print('2')
        cotar.euro()
        montante_n = cotar.e + capital_n
        cadastrar.cadastro_movimentacao(cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n)
        fr5_lab7['text']=montante_n
    if nome_moeda_n == 'LIBRA':
        print('3')
        cotar.libra()
        montante_n = cotar.l + capital_n
        cadastrar.cadastro_movimentacao(cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n)
        fr5_lab7['text']=montante_n
    if nome_moeda_n == 'BITCOIN':
        print('4')
        cotar.bitcoin()
        montante_n = cotar.b + capital_n
        cadastrar.cadastro_movimentacao(cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n)
        fr5_lab7['text']=montante_n
    if nome_moeda_n == 'ETHEREUM':
        print('5')
        cotar.ethereum()
        montante_n = cotar.t + capital_n
        cadastrar.cadastro_movimentacao(cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n)
        fr5_lab7['text']=montante_n

#def escolha_euro2():
#    meses = fr3_in4.get()
#    cotar.euro2(meses)
#    fr2_lab13['text']=cotar.e3
#def escolha_libra2():
#    meses = 
#    cotar.libra2(meses)
#    fr2_lab14['text']=cotar.l3
#def escolha_bitcoin2():
#    meses = 
#    cotar.bitcoin2(meses)
#    fr2_lab15['text']=cotar.b3
#def escolha_ethereum2():
#    meses = 
#    cotar.ethereum1(meses)
#    fr2_lab16['text']=cotar.et3

hello = StringVar()
def mostrar(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)
    feecho =  Button(fr0, image=fr0_img_3,bd=0, command=esconder).place(width=45, height=45, x=436, y=302)
    
def esconder(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)
    fr0_bt3 = Button(fr0, image=fr0_img_3,bd=0, command=mostrar).place(width=45, height=45, x=436, y=302)

hello_1 = StringVar()
def mostrar_1(*args):
    fr1_in1 = Entry(fr1, textvariable=hello_1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=23, y=425)
    feecho = Button(fr1, bd=0, image=fr1_img_3, command=esconder_1).place(width=45, height=40, x=430, y=430)
    
def esconder_1(*args):
    fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=23, y=425)
    fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=430)

# Importar imagens

fr0_img_1 = PhotoImage(file="imagens\\fundo.png")
fr0_img_3 = PhotoImage(file="imagens\\olho.png")
fr0_img_2 = PhotoImage(file="imagens\\entrar.png")
fr0_img_4 = PhotoImage(file="imagens\\cadastro.png")

fr0_img_1 = PhotoImage(file="imagens\\fundo.png")
fr0_img_3 = PhotoImage(file="imagens\\olho.png")
fr0_img_2 = PhotoImage(file="imagens\\entrar.png")
fr0_img_4 = PhotoImage(file="imagens\\cadastro.png")


#frame 1
fr1_img_1 = PhotoImage(file="imagens\\cadastrar.png")
fr1_img_2 = PhotoImage(file="imagens\\fundo2.png")
fr1_img_3 = PhotoImage(file="imagens\\olho.png")
fr1_img_4 = PhotoImage(file="imagens\\voltar.png")
fr1_img_5 = PhotoImage(file="imagens\\olho.png")

#frame 2
fr2_img_1 = PhotoImage(file="imagens\\tela.png")
fr2_img_2 = PhotoImage(file="imagens\\guardar.png")
fr2_img_3 = PhotoImage(file="imagens\\comprar.png")
fr2_img_4 = PhotoImage(file="imagens\\vender.png")
fr2_img_5 = PhotoImage(file="imagens\\tabela.png")
fr2_img_6 = PhotoImage(file="imagens\\grafico.png")
fr2_img_7 = PhotoImage(file="imagens\\moedas.png")
fr2_img_8 = PhotoImage(file="imagens\\cotação do dia.png")
fr2_img_9 = PhotoImage(file="imagens\\media.png")
fr2_img_10 =  PhotoImage(file="imagens\\fundo 3.png")
fr2_img_11 =  PhotoImage(file="imagens\\sair.png")

##frame 3
#fr3_img_1 = PhotoImage(file="imagens\\tela.png")
#fr3_img_2 = PhotoImage(file="imagens\\guardar.png")
#fr3_img_3 = PhotoImage(file="imagens\\comprar.png")
#fr3_img_4 = PhotoImage(file="imagens\\vender.png")
#fr3_img_5 = PhotoImage(file="imagens\\tabela.png")
#fr3_img_6 = PhotoImage(file="imagens\\compra.png")
#fr3_img_7 = PhotoImage(file="imagens\\comprar.png")
#fr3_img_8 = PhotoImage(file="imagens\\limpa.png")
#fr3_img_9 = PhotoImage(file="imagens\\confirmar.png")
#fr3_img_10 = PhotoImage(file="imagens\\grafico.png")
#fr3_img_11 = PhotoImage(file="imagens\\moedas.png")
#fr3_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
#fr3_img_13 = PhotoImage(file="imagens\\media.png")
#fr3_img_14 = PhotoImage(file="imagens\\volta.png")

#frame 4
fr4_img_1 = PhotoImage(file="imagens\\tela.png")
fr4_img_2 = PhotoImage(file="imagens\\guardar.png")
fr4_img_3 = PhotoImage(file="imagens\\comprar.png")
fr4_img_4 = PhotoImage(file="imagens\\vender.png")
fr4_img_5 = PhotoImage(file="imagens\\tabela.png")
fr4_img_6= PhotoImage(file="imagens\\venda.png")
fr4_img_8 = PhotoImage(file="imagens\\limpa.png")
fr4_img_9 = PhotoImage(file="imagens\\confirmar.png")
fr4_img_10 = PhotoImage(file="imagens\\grafico.png")
fr4_img_11 = PhotoImage(file="imagens\\moedas.png")
fr4_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
fr4_img_13 = PhotoImage(file="imagens\\media.png")
fr4_img_14 = PhotoImage(file="imagens\\volta.png")

#frame 5
fr5_img_1 = PhotoImage(file="imagens\\tela.png")
fr5_img_2 = PhotoImage(file="imagens\\guardar.png")
fr5_img_3 = PhotoImage(file="imagens\\comprar.png")
fr5_img_4 = PhotoImage(file="imagens\\vender.png")
fr5_img_5 = PhotoImage(file="imagens\\tabela.png")
fr5_img_6= PhotoImage(file="imagens\\investir.png")
fr5_img_8 = PhotoImage(file="imagens\\limpa.png")
fr5_img_9 = PhotoImage(file="imagens\\confirmar.png")
fr5_img_10 = PhotoImage(file="imagens\\grafico.png")
fr5_img_11 = PhotoImage(file="imagens\\moedas.png")
fr5_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
fr5_img_13 = PhotoImage(file="imagens\\media.png")
fr5_img_14 = PhotoImage(file="imagens\\volta.png")
#frame 6

# Criação de labels 

#tela de fundo da tela de login

fr0_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)


# Criação de caixas de entrada  

#frame 0 Tela de login

#entre do cpf e cnpj                                                                                                                                                                                                                                                                                                                                                                                                               
fr0_in2 = Entry(fr0, bd=2, font=("Calibri", 15), justify=CENTER)
fr0_in2.place(width=392, height=45, x=37, y=185)
fr0_in2.bind('<KeyRelease>', cpf)
#fr0_in2.bind('<KeyRelease>', cnpj)

#Entre da senha

#CONTRUÇÃO EWERSON
fr0_in3 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
fr0_in3.place(width=392, height=45, x=37, y=302)
#CONTRUÇÃO EWERSON

# Criação de botões 

#CONSTRUÇÃO EWERSON
# Botão do entrar
fr0_bt0 = Button(fr0, bd=0, image=fr0_img_2,command=lambda: [logando(), chama_cotacao(), chama_media(),clear_4()])
fr0_bt0.place(width=118, height=64, x=290, y=408)

# Botão do cadastro
fr0_bt2 = Button(fr0, bd=0, image=fr0_img_4 , command=lambda: [fr0.grid_remove(), fr1.grid()]).place(width=174, height=64, x=63, y=408)
#CONSTRUÇÃO EWERSON

# Botão do olho
fr0_bt3 = Button(fr0, bd=0, image=fr0_img_3, command=mostrar).place(width=45, height=45, x=436, y=302)


# Frame 1 Tela de Cadastro

# Criação de labels 

#tela de fundo do Cadastro
fr1_lab2 = Label(fr1, image=fr1_img_2,width=480).grid(row=0,column=0) 

# Criação de caixas de entrada 

#entre do cpf e cnpj
fr1_in0 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in0.place(width=392, height=45, x=20, y=130)
fr1_in0.bind('<KeyRelease>', cpf_1)
#fr1_in0.bind('<KeyRelease>', cnpj_1)

#Entre da senha  
fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in1.place(width=392, height=45, x=23, y=425)


#Entre do Nome
fr1_in2 = Entry(fr1, bd=2, textvariable=var5,font=("Calibri", 15), justify=CENTER)
fr1_in2.place(width=392, height=45, x=20, y=202)
fr1_in2.bind('<KeyRelease>', nome)

#Entre do Data de Nascimento
fr1_in3 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in3.place(width=392, height=45, x=22, y=273)
fr1_in3.bind('<KeyRelease>', data_nasc)

#Entre do telefone
fr1_in4 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in4.place(width=392, height=45, x=22, y=343)
fr1_in4.bind('<KeyRelease>', telefone_cadastro)

# Criação de botões 


# Botão do Cadastrar
fr1_bt0 = Button(fr1, bd=0, image=fr1_img_1, command=lambda: [fazer_cadastro(),fr1.grid_remove(), fr0.grid()])
fr1_bt0.place(width=173, height=64, x=265, y=488) #Cadastrar

# Botão do olho
fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=430) #Olho

# Botão do Voltar
fr1_bt2 = Button(fr1, bd=0, image=fr1_img_4 , command=lambda: [fr1.grid_remove(), fr0.grid()]).place(width=170, height=58, x=46, y=491) #Voltar


# frame 2 Tela do investidor

# Criação de labels 

fr2_lab = Label(fr2, image=fr2_img_1, width=1285).grid(row=0,column=0,sticky=W)

fr2_lab1 = Label(fr2,bd=0, image=fr2_img_5).place(width=305, height=65, x=974, y=26)

fr2_lab2 = Label(fr2, image=fr2_img_6, width=1000).place(width=950, height=470, x=5, y=125) # grafico

fr2_lab3 = Label(fr2,bd=0, image=fr2_img_7).place(width=178, height=52, x=30, y=148) # label moeda

fr2_lab4 = Label(fr2,bd=0, image=fr2_img_8).place(width=218, height=52, x=222, y=148) # label cotação

fr2_lab5 = Label(fr2,bd=0, image=fr2_img_9).place(width=480, height=52, x=462, y=148) # label media

fr2_lab6 = Label(fr2, image=fr2_img_10,bd=0)
fr2_lab6.place(width=310, height=470, x=970, y=130)

fr2_lab7 = Label(fr2, text='',bd=0)
fr2_lab7.place(width=200, height=40, x=230, y=225) #label do USD

fr2_lab8 = Label(fr2, text='',bd=0)
fr2_lab8.place(width=200, height=40, x=230, y=307) #label do EURO

fr2_lab9 = Label(fr2, text='',bd=0)
fr2_lab9.place(width=200, height=40, x=230, y=380) #label do Libra

fr2_lab10 = Label(fr2, text='',bd=0)
fr2_lab10.place(width=200, height=40, x=230, y=460) #label do Bitcoin

fr2_lab11 = Label(fr2, text='',bd=0)
fr2_lab11.place(width=200, height=40, x=230, y=535) #label do Ethereum

fr2_lab12 = Label(fr2, text='',bd=0)
fr2_lab12.place(width=465, height=40, x=470, y=225) #label do USD Média

fr2_lab13 = Label(fr2, text='',bd=0)
fr2_lab13.place(width=465, height=40, x=470, y=307) #label do Euro Média

fr2_lab14 = Label(fr2, text='',bd=0)
fr2_lab14.place(width=465, height=40, x=470, y=380) #label do Libra Média

fr2_lab15 = Label(fr2, text='',bd=0)
fr2_lab15.place(width=465, height=40, x=470, y=460) #label do Bitcoin Média

fr2_lab16 = Label(fr2, text='',bd=0)
fr2_lab16.place(width=465, height=40, x=470, y=535) #label do ETHEREUM Média

fr2_lab17 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab17.place(width=145, height=24, x=991, y=191) #Nome

fr2_lab18 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab18.place(width=145, height=24, x=991, y=252) #Dólar

fr2_lab19 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab19.place(width=145, height=24, x=991, y=308) #Euro

fr2_lab20 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab20.place(width=145, height=24, x=991, y=360) #libra

fr2_lab21 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab21.place(width=145, height=24, x=991, y=416) #Bitcoin

fr2_lab22 = Label(fr2, text='', font=("Calibri", 15))
fr2_lab22.place(width=145, height=24, x=991, y=472) #Ethereum

# Criação de botões

# Botão de guardar
fr2_bt1 = Button(fr2, bd=0, image=fr2_img_2, command= lambda:[fr2.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=525, y=32)
# Botão de comprar
#fr2_bt2 = Button(fr2, bd=0, image=fr2_img_3, command= lambda:[fr2.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de vender
fr2_bt3 = Button(fr2, bd=0, image=fr2_img_4, command= lambda:[fr2.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=158, y=32)
# Botão de Sair
fr2_bt4 = Button(fr2,bd=0,image=fr2_img_11, command= lambda:[fr2.grid_remove(),fr0.grid(),root.geometry("484x560+800+155")])
fr2_bt4.place(width=115, height=42, x=1070, y=518)

# frame 3 # tela da Compra

# Criação de labels 


## tela do Investidor de Compra
#fr3_lab = Label(fr3, image=fr3_img_1, width=1285).grid(row=0,column=0,sticky=W)
#
## imagem compra
#fr3_lab1 = Label(fr3, image=fr3_img_6,bd=0).place(width=310, height=470, x=970, y=130)
#
## image tabela
#fr3_lab2 = Label(fr3,bd=0, image=fr3_img_5).place(width=305, height=65, x=974, y=26)
##tela do grafico
#fr3_lab3 = Label(fr3, image=fr3_img_10, width=1000).place(width=950, height=470, x=5, y=125) # 
#
#
#fr3_lab4 = Label(fr3,bd=0, image=fr3_img_11).place(width=178, height=52, x=30, y=148) # label moeda
#
#fr3_lab5 = Label(fr3,bd=0, image=fr3_img_12).place(width=218, height=52, x=222, y=148) # label cotação
#
#fr3_lab6 = Label(fr3,bd=0, image=fr3_img_13).place(width=480, height=52, x=462, y=148) # label media
#
#fr3_lab7 = Label(fr3, text='', font=("Calibri", 15))
#fr3_lab7.place(width=145, height=24, x=995, y=400) #Montante
#
#fr3_lab8 = Label(fr3, text='',bd=0)
#fr3_lab8.place(width=200, height=40, x=230, y=225) #label do USD
#
#fr3_lab9 = Label(fr3, text='',bd=0)
#fr3_lab9.place(width=200, height=40, x=230, y=307) #label do EURO
#
#fr3_lab10 = Label(fr3, text='',bd=0)
#fr3_lab10.place(width=200, height=40, x=230, y=380) #label do Libra
#
#fr3_lab11 = Label(fr3, text='',bd=0)
#fr3_lab11.place(width=200, height=40, x=230, y=460) #label do Bitcoin
#
#fr3_lab12 = Label(fr3, text='',bd=0)
#fr3_lab12.place(width=200, height=40, x=230, y=535) #label do Ethereum
#
#fr3_lab13 = Label(fr3, text='',bd=0)
#fr3_lab13.place(width=465, height=40, x=470, y=225) #label do USD Média
#
#fr3_lab14 = Label(fr3, text='',bd=0)
#fr3_lab14.place(width=465, height=40, x=470, y=307) #label do Euro Média
#
#fr3_lab15 = Label(fr3, text='',bd=0)
#fr3_lab15.place(width=465, height=40, x=470, y=380) #label do Libra Média
#
#fr3_lab16 = Label(fr3, text='',bd=0)
#fr3_lab16.place(width=465, height=40, x=470, y=460) #label do Bitcoin Média
#
#fr3_lab17 = Label(fr3, text='',bd=0)
#fr3_lab17.place(width=465, height=40, x=470, y=535) #label do ETHEREUM Média
#
#
## Criação de botões 
#
## Botão de guardar
#fr3_bt1 = Button(fr3, bd=0, image=fr3_img_2, command= lambda:[fr3.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=675, y=32)
## Botão de comprar
#fr3_bt2 = Button(fr3, bd=0, image=fr3_img_3, command= lambda:[fr3.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
## Botão de vender
#fr3_bt3 = Button(fr3, bd=0, image=fr3_img_4, command= lambda:[fr3.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=367, y=32)
## Botão de limpar
#fr3_bt4 = Button(fr3, bd=0, image=fr3_img_8, command=lambda: [clear_1()])
#fr3_bt4.place(width=115, height=43, x=996, y=461)
#
##  botão de Confirmar
#fr3_bt5 = Button(fr3, bd=0, image=fr3_img_9, command=lambda: [escolha_guardar()])
#fr3_bt5.place(width=115, height=42, x=1137, y=462)
#
## Botão de voltar
#fr3_bt6 = Button(fr3, bd=0, image=fr3_img_14, command=lambda: [fr3.grid_remove(),fr2.grid(),root.geometry("1289x600+310+153")])
#fr3_bt6.place(width=115, height=42, x=1069, y=524)
#
#fr3_in1 = Entry(fr3,bd=2,textvariable=var1, font=("Calibri", 15))
#fr3_in1.place(width=140, height=24, x=995, y=200) 
#fr3_in1.bind("<KeyRelease>")#,comprar_confirmar)   #moedaa
#
#fr3_in2 = Entry(fr3, bd=2, font=("Calibri", 15))
#fr3_in2.place(width=140, height=24, x=995, y=265) #capital
#fr3_in2.bind("<KeyRelease>", comprar_capital) #capital
#
#fr3_in4 = Entry(fr3, bd=2, font=("Calibri", 15))
#fr3_in4.place(width=145, height=24, x=995, y=325) #Tempo
#fr3_in4.bind("<KeyRelease>", compra_tempo) #Tempo


# frame 4 # tela da Venda

# Criação de labels 

# tela do Investidor de Compra
fr4_lab = Label(fr4, image=fr4_img_1, width=1285).grid(row=0,column=0,sticky=W)

# imahem compra
fr4_lab1 = Label(fr4,bd=0, image=fr4_img_6).place(width=310, height=470, x=970, y=130)

# image tabela
fr4_lab2 = Label(fr4,bd=0, image=fr4_img_5).place(width=305, height=65, x=974, y=26)

#tela do grafico
fr4_lab3 = Label(fr4, image=fr4_img_10, width=1000).place(width=950, height=470, x=5, y=125) # 

fr4_lab4 = Label(fr4,bd=0, image=fr4_img_11).place(width=178, height=52, x=30, y=148) # label moeda

fr4_lab5 = Label(fr4,bd=0, image=fr4_img_12).place(width=218, height=52, x=222, y=148) # label cotação

fr4_lab6 = Label(fr4,bd=0, image=fr4_img_13).place(width=480, height=52, x=462, y=148) # label media

fr4_lab7 = Label(fr4,text='', font=("Calibri", 15))
fr4_lab7.place(width=145, height=24, x=993, y=370) #Montante

fr4_lab8 = Label(fr4, text='',bd=0)
fr4_lab8.place(width=200, height=40, x=230, y=225) #label do USD

fr4_lab9 = Label(fr4, text='',bd=0)
fr4_lab9.place(width=200, height=40, x=230, y=307) #label do EURO

fr4_lab10 = Label(fr4, text='',bd=0)
fr4_lab10.place(width=200, height=40, x=230, y=380) #label do Libra

fr4_lab11 = Label(fr4, text='',bd=0)
fr4_lab11.place(width=200, height=40, x=230, y=460) #label do Bitcoin

fr4_lab12 = Label(fr4, text='',bd=0)
fr4_lab12.place(width=200, height=40, x=230, y=535) #label do Ethereum

fr4_lab13 = Label(fr4, text='',bd=0)
fr4_lab13.place(width=465, height=40, x=470, y=225) #label do USD Média

fr4_lab14 = Label(fr4, text='',bd=0)
fr4_lab14.place(width=465, height=40, x=470, y=307) #label do Euro Média

fr4_lab15 = Label(fr4, text='',bd=0)
fr4_lab15.place(width=465, height=40, x=470, y=380) #label do Libra Média

fr4_lab16 = Label(fr4, text='',bd=0)
fr4_lab16.place(width=465, height=40, x=470, y=460) #label do Bitcoin Média

fr4_lab17 = Label(fr4, text='',bd=0)
fr4_lab17.place(width=465, height=40, x=470, y=535) #label do ETHEREUM Média


# Criação de botões 

# Botão de guardar
fr4_bt1 = Button(fr4, bd=0, image=fr4_img_2, command= lambda:[fr4.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=525, y=32)
# Botão de comprar
#fr4_bt2 = Button(fr4, bd=0, image=fr4_img_3, command= lambda:[fr4.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de vender
fr4_bt3 = Button(fr4, bd=0, image=fr4_img_4, command= lambda:[fr4.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=158, y=32)

# Botão de limpar
fr4_bt4 = Button(fr4, bd=0, image=fr4_img_8, command=lambda: [clear_2()] )
fr4_bt4.place(width=115, height=43, x=1002, y=432)
#  botão de Confirmar
fr4_bt5 = Button(fr4, bd=0, image=fr4_img_9, command=lambda: [escolha_vender()])
fr4_bt5.place(width=115, height=42, x=1141, y=432)

# Botão de voltar
fr4_bt6 = Button(fr4, bd=0, image=fr4_img_14, command=lambda: [fr4.grid_remove(),fr2.grid(),root.geometry("1289x600+310+153")])
fr4_bt6.place(width=115, height=42, x=1075, y=498)

fr4_in1 = Entry(fr4, bd=2,textvariable=var2, font=("Calibri", 15))
fr4_in1.place(width=140, height=24, x=993, y=222) #moeda a vender
fr4_in1.bind("<KeyRelease>", vender) 

fr4_in2 = Entry(fr4, bd=2, font=("Calibri", 15))
fr4_in2.place(width=140, height=24, x=993, y=287) #capital
fr4_in2.bind("<KeyRelease>", venda_capital) 

#fr4_in3 = Entry(fr4,textvariable=var3, bd=2, font=("Calibri", 15))
#fr4_in3.bind("<KeyRelease>")
#fr4_in3.place(width=145, height=24, x=993, y=390) #moeda a comprar

# frame 5 Tela de Guardar

# Criação de labels 

# tela do Investidor de Guardar
fr5_lab = Label(fr5, image=fr5_img_1, width=1285).grid(row=0,column=0,sticky=W) # imagem de fundo

# imagem do moeda e investir
fr5_lab1 = Label(fr5,bd=0, image=fr5_img_6).place(width=310, height=470, x=970, y=130)

# imagem Tabela 
fr5_lab2 = Label(fr5,bd=0, image=fr5_img_5).place(width=305, height=65, x=974, y=26)

#tela do grafico
fr5_lab3 = Label(fr5, image=fr5_img_10, width=1000).place(width=950, height=470, x=5, y=125) #

fr5_lab4 = Label(fr5,bd=0, image=fr5_img_11).place(width=178, height=52, x=30, y=148) # label moeda

fr5_lab5 = Label(fr5,bd=0, image=fr5_img_12).place(width=218, height=52, x=222, y=148) # label cotação

fr5_lab6 = Label(fr5,bd=0, image=fr5_img_13).place(width=480, height=52, x=462, y=148) # label media

fr5_lab7 = Label(fr5,text= '', font=("Calibri", 15))
fr5_lab7.place(width=145, height=24, x=991, y=416) #Montante

fr5_lab8 = Label(fr5, text='',bd=0)
fr5_lab8.place(width=200, height=40, x=230, y=225) #label do USD

fr5_lab9 = Label(fr5, text='',bd=0)
fr5_lab9.place(width=200, height=40, x=230, y=307) #label do EURO

fr5_lab10 = Label(fr5, text='',bd=0)
fr5_lab10.place(width=200, height=40, x=230, y=380) #label do Libra

fr5_lab11 = Label(fr5, text='',bd=0)
fr5_lab11.place(width=200, height=40, x=230, y=460) #label do Bitcoin

fr5_lab12 = Label(fr5, text='',bd=0)
fr5_lab12.place(width=200, height=40, x=230, y=535) #label do Ethereum

fr5_lab13 = Label(fr5, text='',bd=0)
fr5_lab13.place(width=465, height=40, x=470, y=225) #label do USD Média

fr5_lab14 = Label(fr5, text='',bd=0)
fr5_lab14.place(width=465, height=40, x=470, y=307) #label do Euro Média

fr5_lab15 = Label(fr5, text='',bd=0)
fr5_lab15.place(width=465, height=40, x=470, y=380) #label do Libra Média

fr5_lab16 = Label(fr5, text='',bd=0)
fr5_lab16.place(width=465, height=40, x=470, y=460) #label do Bitcoin Média

fr5_lab17 = Label(fr5, text='',bd=0)
fr5_lab17.place(width=465, height=40, x=470, y=535) #label do ETHEREUM Média

# Criação de botões 

# Botão de guardar
fr5_bt1 = Button(fr5, bd=0, image=fr5_img_2, command= lambda:[fr5.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=525, y=32)
# Botão de compra
#fr5_bt2 = Button(fr5, bd=0, image=fr5_img_3,command= lambda:[fr5.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de venda
fr5_bt3 = Button(fr5, bd=0, image=fr5_img_4,command= lambda:[fr5.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=158, y=32)
# Botão de limpar
fr5_bt4 = Button(fr5, bd=0, image=fr5_img_8, command=lambda: [clear_3()])
fr5_bt4.place(width=115, height=42, x=996, y=459)
#  botão de Confirmar
fr5_bt5 = Button(fr5, bd=0, image=fr5_img_9, command=lambda: [escolha_guardar()])
fr5_bt5.place(width=115, height=42, x=1130, y=460)
# Botão de voltar
fr5_bt6 = Button(fr5, bd=0, image=fr4_img_14, command=lambda: [fr5.grid_remove(),fr2.grid(),root.geometry("1289x600+310+153")])
fr5_bt6.place(width=115, height=42, x=1062, y=525)
fr5_in1 = Entry(fr5, bd=2,textvariable=var4, font=("Calibri", 15))
fr5_in1.place(width=140, height=24, x=992, y=222) #moeda a Inserir

fr5_in2 = Entry(fr5, bd=2, font=("Calibri", 15))
fr5_in2.place(width=140, height=24, x=992, y=287) #capital
fr5_in2.bind("<KeyRelease>",guarda_capital)

fr5_in3 = Entry(fr5, bd=2, font=("Calibri", 15))
fr5_in3.place(width=145, height=24, x=990, y=348) 
fr5_in3.bind("<KeyRelease>",guarda_tempo)#Tempo



fr0.grid()
root.mainloop()